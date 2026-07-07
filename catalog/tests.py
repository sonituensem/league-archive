from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.forms import ChampionForm
from catalog.models import Champion, Region, Role


User = get_user_model()


class ModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.region = Region.objects.create(
            name="Demacia",
            description="A powerful kingdom.",
        )

        cls.role = Role.objects.create(
            name="Fighter",
            description="Close combat champion.",
        )

        cls.champion = Champion.objects.create(
            name="Garen",
            title="The Might of Demacia",
            description="A warrior of Demacia.",
            difficulty=3,
            release_date=date(2010, 1, 1),
            region=cls.region,
        )

        cls.champion.roles.add(cls.role)

    def test_region_str(self):
        self.assertEqual(
            str(self.region),
            "Demacia",
        )

    def test_role_str(self):
        self.assertEqual(
            str(self.role),
            "Fighter",
        )

    def test_champion_str(self):
        self.assertEqual(
            str(self.champion),
            "Garen",
        )

    def test_champion_relationships(self):
        self.assertEqual(
            self.champion.region,
            self.region,
        )

        self.assertIn(
            self.role,
            self.champion.roles.all(),
        )


class FormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.region = Region.objects.create(
            name="Noxus",
            description="Military nation.",
        )

        cls.role = Role.objects.create(
            name="Fighter",
            description="Close combat champion.",
        )

    def test_valid_difficulty(self):
        form = ChampionForm(
            data={
                "name": "Darius",
                "title": "Hand of Noxus",
                "description": "Powerful warrior.",
                "difficulty": 5,
                "release_date": "2012-01-01",
                "region": self.region.id,
                "roles": [self.role.id],
            }
        )

        print(form.errors)
        self.assertTrue(
            form.is_valid()
        )

    def test_invalid_difficulty(self):
        form = ChampionForm(
            data={
                "name": "Darius",
                "title": "Hand of Noxus",
                "description": "Powerful warrior.",
                "difficulty": 15,
                "release_date": "2012-01-01",
                "region": self.region.id,
                "roles": [self.role.id],
            }
        )

        self.assertFalse(
            form.is_valid()
        )


class AuthenticationTests(TestCase):

    def test_user_registration(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "testuser",
                "password1": "StrongPassword123!",
                "password2": "StrongPassword123!",
            },
        )

        self.assertRedirects(
            response,
            reverse("login"),
        )

        self.assertTrue(
            User.objects.filter(
                username="testuser",
            ).exists()
        )

    def test_user_login(self):
        User.objects.create_user(
            username="testuser",
            password="StrongPassword123!",
        )

        logged_in = self.client.login(
            username="testuser",
            password="StrongPassword123!",
        )

        self.assertTrue(
            logged_in
        )


class ChampionViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.region = Region.objects.create(
            name="Ionia",
            description="Mystical land.",
        )

        cls.role = Role.objects.create(
            name="Mage",
            description="Magic user.",
        )

        cls.champion = Champion.objects.create(
            name="Ahri",
            title="Nine-Tailed Fox",
            description="Mage champion.",
            difficulty=4,
            release_date=date(2011, 1, 1),
            region=cls.region,
        )

        cls.champion.roles.add(cls.role)

    def test_champion_list_view(self):
        response = self.client.get(
            reverse("champion-list"),
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertIn(
            self.champion,
            response.context["champions"],
        )

    def test_champion_detail_view(self):
        response = self.client.get(
            reverse(
                "champion-detail",
                args=[self.champion.id],
            ),
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_create_champion(self):
        response = self.client.post(
            reverse("champion-create"),
            {
                "name": "Lux",
                "title": "Lady of Luminosity",
                "description": "Mage champion.",
                "difficulty": 5,
                "release_date": "2010-01-01",
                "region": self.region.id,
                "roles": [self.role.id],
            },
        )

        self.assertRedirects(
            response,
            reverse("champion-list"),
        )

        self.assertTrue(
            Champion.objects.filter(
                name="Lux",
            ).exists()
        )

    def test_update_champion(self):
        response = self.client.post(
            reverse(
                "champion-update",
                args=[self.champion.id],
            ),
            {
                "name": "Ahri Updated",
                "title": "Updated title",
                "description": "Updated description.",
                "difficulty": 5,
                "release_date": "2011-01-01",
                "region": self.region.id,
                "roles": [self.role.id],
            },
        )

        self.assertRedirects(
            response,
            reverse("champion-list"),
        )

        self.champion.refresh_from_db()

        self.assertEqual(
            self.champion.name,
            "Ahri Updated",
        )

    def test_delete_champion(self):
        response = self.client.post(
            reverse(
                "champion-delete",
                args=[self.champion.id],
            ),
        )

        self.assertRedirects(
            response,
            reverse("champion-list"),
        )

        self.assertFalse(
            Champion.objects.filter(
                id=self.champion.id,
            ).exists()
        )

    def test_search_champion(self):
        response = self.client.get(
            reverse("champion-list"),
            {
                "query": "Ahri",
            },
        )

        self.assertIn(
            self.champion,
            response.context["champions"],
        )

    def test_filter_champion_by_region(self):
        response = self.client.get(
            reverse("champion-list"),
            {
                "region": self.region.id,
            },
        )

        self.assertIn(
            self.champion,
            response.context["champions"],
        )

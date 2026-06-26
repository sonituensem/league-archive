from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Champion, Region, Role, Skin, User


class ChampionAdminForm(forms.ModelForm):
    class Meta:
        model = Champion
        fields = "__all__"

    def clean_difficulty(self) -> int:
        difficulty = self.cleaned_data["difficulty"]

        if not 1 <= difficulty <= 10:
            raise forms.ValidationError(
                "Difficulty must be between 1 and 10."
            )

        return difficulty


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    form = ChampionAdminForm

    list_display = (
        "name",
        "title",
        "region",
        "difficulty",
        "release_year",
    )

    search_fields = (
        "name",
        "title",
    )

    list_filter = (
        "region",
        "roles",
        "difficulty",
    )

    filter_horizontal = (
        "roles",
    )


@admin.register(Skin)
class SkinAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "champion",
        "release_year",
    )

    search_fields = (
        "name",
        "champion__name",
    )

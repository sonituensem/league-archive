from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    pass


class Region(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    image = models.ImageField(
        upload_to="roles/",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name


class Champion(models.Model):
    name = models.CharField(max_length=100)

    title = models.CharField(
        max_length=150,
    )

    description = models.TextField()


    image = models.ImageField(
        upload_to="champions/",
        null=True,
        blank=True,
    )


    image_position = models.CharField(
        max_length=50,
        default="center center",
    )


    difficulty = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        default=1,
    )


    release_date = models.DateField()


    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="champions",
    )


    roles = models.ManyToManyField(
        Role,
        related_name="champions",
    )


    class Meta:
        ordering = ["name"]


    def __str__(self) -> str:
        return self.name



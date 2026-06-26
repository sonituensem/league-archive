from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    pass


class Region(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Champion(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()

    difficulty = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        default=1,
    )

    release_year = models.PositiveIntegerField()

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="champions",
    )

    roles = models.ManyToManyField(
        Role,
        related_name="champions",
    )

    def __str__(self) -> str:
        return self.name
    
class Skin(models.Model):
    name = models.CharField(max_length=150)

    release_year = models.PositiveIntegerField()

    champion = models.ForeignKey(
        Champion,
        on_delete=models.CASCADE,
        related_name="skins",
    )

    def __str__(self) -> str:
        return self.name

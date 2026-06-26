from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Champion, Region, Role, Skin, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
        "region",
        "difficulty",
        "release_year",
    )
    search_fields = ("name", "title")
    list_filter = ("region", "roles")


@admin.register(Skin)
class SkinAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "champion",
        "release_year",
    )
    search_fields = ("name",)
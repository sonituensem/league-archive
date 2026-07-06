from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import (
    Champion,
    Region,
    Role,
    User,
)


class ChampionAdminForm(forms.ModelForm):

    class Meta:
        model = Champion

        fields = "__all__"

        widgets = {
            "difficulty": forms.NumberInput(
                attrs={
                    "min": 1,
                    "max": 10,
                }
            ),

            "release_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }


    def clean_difficulty(self):

        difficulty = self.cleaned_data["difficulty"]

        if not 1 <= difficulty <= 10:
            raise forms.ValidationError(
                "Difficulty must be between 1 and 10."
            )

        return difficulty





@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
    )





@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )





@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "image_preview",
    )

    search_fields = (
        "name",
    )


    def image_preview(self, obj):

        if obj.image:

            return "✓"

        return "-"


    image_preview.short_description = "Image"





@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):

    form = ChampionAdminForm


    list_display = (
        "name",
        "title",
        "region",
        "difficulty",
        "release_date",
        "roles_count",
    )


    search_fields = (
        "name",
        "title",
    )


    list_filter = (
        "region",
        "roles",
        "difficulty",
        "release_date",
    )


    filter_horizontal = (
        "roles",
    )


    ordering = (
        "name",
    )


    readonly_fields = (
        "roles_count",
    )


    def roles_count(self, obj):

        return obj.roles.count()


    roles_count.short_description = "Roles"


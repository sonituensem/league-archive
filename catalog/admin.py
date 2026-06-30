from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import (
    Champion,
    Region,
    Role,
    Skin,
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
    pass





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
        "image",
    )


    search_fields = (
        "name",
    )





@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):

    form = ChampionAdminForm


    list_display = (
        "name",
        "title",
        "region",
        "difficulty",
        "release_date",
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





@admin.register(Skin)
class SkinAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "champion",
        "release_date",
    )


    search_fields = (
        "name",
        "champion__name",
    )

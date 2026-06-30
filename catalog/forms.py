from django import forms

from catalog.models import Champion


class ChampionForm(forms.ModelForm):
    class Meta:
        model = Champion

        fields = [
            "name",
            "title",
            "description",
            "image",
            "image_position",
            "difficulty",
            "release_date",
            "region",
            "roles",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                }
            ),
            "release_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "difficulty": forms.NumberInput(
                attrs={
                    "min": 1,
                    "max": 10,
                }
            ),
            "roles": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                }
            ),
        }

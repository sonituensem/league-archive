from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Champion, User


class ChampionForm(forms.ModelForm):
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


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )

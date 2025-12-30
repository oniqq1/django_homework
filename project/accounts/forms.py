from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class UserCreatingForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            )

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter email"}
            ),
        }

    username = forms.CharField(
        required=True,
        label="Username",
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        ),
    )

    email = forms.EmailField(
        required=True,
        label="Email",
        max_length=60,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter email"}
        ),
    )

    password1 = forms.CharField(
        max_length=20,
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
    )

    password2 = forms.CharField(
        max_length=20,
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirmed entered password"}
        ),
    )

    is_staff = forms.BooleanField(
        required=False,
        label="Staff status",
    )

    def clean_password2(self) -> str:
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords dont match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if self.cleaned_data.get('is_staff'):
            user.is_staff = True
            user.is_superuser = True
        if commit:
            user.save()
        return user


class AuthForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="Username",
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        ),
    )

    password = forms.CharField(
        max_length=20,
        label="Password",
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
    )
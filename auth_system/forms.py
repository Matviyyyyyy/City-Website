from django import forms
from auth_system.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    media = forms.ImageField(
        required=False,
        validators=[validate_image_size],
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "phone_number", "media")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ім'я..."
        })
        self.fields["first_name"].label = ""

        self.fields["last_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Прізвище..."
        })
        self.fields["last_name"].label = ""

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Електронна пошта..."
        })
        self.fields["email"].label = ""

        self.fields["phone_number"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Номер телефону..."
        })
        self.fields["phone_number"].label = ""

        self.fields['password1'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Пароль..."
        })
        self.fields["password1"].label = ""

        self.fields['username'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ім'я користувача..."
        })
        self.fields["username"].label = ""

        self.fields['password2'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Підтвердьте пароль..."
        })
        self.fields["password2"].label = ""



class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ім'я користувача..."
        })
        self.fields["username"].label = ""

        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ім'я користувача..."
        })
        self.fields["password"].label = ""

class UserForm(forms.ModelForm):
    media = forms.ImageField(
        required=False,
        validators=[validate_image_size],
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name", "last_name", "email", "phone_number", "media"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ім'я..."
        })
        self.fields["first_name"].label = ""

        self.fields["last_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Прізвище..."
        })
        self.fields["last_name"].label = ""

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Електронна пошта..."
        })
        self.fields["email"].label = ""

        self.fields["phone_number"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Номер телефону..."
        })
        self.fields["phone_number"].label = ""



class UserRoleForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("role",)

    def __init__(self, *args, **kwargs):
        super(UserRoleForm, self).__init__(*args, **kwargs)
        self.fields["role"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Роль..."
        })
        self.fields["role"].label = ""


from django import forms
from adverts.models import *
from adverts.validators import validate_image_size
class AdvertForm(forms.ModelForm):
    media = forms.FileField(
        required=False,
        validators=[validate_image_size],
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Advert
        fields = ["text", "title", "duration", "media"]

    def __init__(self, *args, **kwargs):
        super(AdvertForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Текст..."
        })
        self.fields["text"].label = ""

        self.fields["duration"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Тривалість..."
        })
        self.fields["duration"].label = ""

        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Заголовок..."
        })
        self.fields["title"].label = ""

        self.fields["media"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Фото..."
        })
        self.fields["media"].label = ""

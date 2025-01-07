from django import forms
from news.models import *
from news.validators import validate_image_size
class NewForm(forms.ModelForm):
    file = forms.FileField(
        required=False,
        validators=[validate_image_size],
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = New
        fields = ["title", "text", "type", "file"]

    def __init__(self, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Заголовок..."
        })
        self.fields["title"].label = ""

        self.fields["text"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Текст..."
        })
        self.fields["text"].label = ""

        self.fields["type"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Тип..."
        })
        self.fields["type"].label = "Тип:"

        self.fields["file"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Файл..."
        })
        self.fields["file"].label = "Файл:"



class NewsFilterForm(forms.Form):
    TYPE_CHOICES = [
        ("", "All"),
        ('sport', 'Sport'),
        ('policy', 'Policy'),
        ('inf', 'Infrastructure'),
        ('life', 'Life')
    ]

    type = forms.ChoiceField(choices=TYPE_CHOICES, required=False, label="")

    def __init__(self, *args, **kwargs):
        super(NewsFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
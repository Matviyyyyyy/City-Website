from django import forms
from institutions.models import *
from institutions.validators import validate_image_size

class InstitutionFilterForm(forms.Form):
    TYPE_CHOICES = [
        ('catering', 'Catering'),
        ('sport', 'Sport'),
        ('entertainment', 'Entertainment'),
        ('education', 'Education'),
        ('trade', 'Trade'),
        ('hotels', 'Hotels'),
        ('beauty_health', 'Beauty and health'),
    ]

    type = forms.ChoiceField(choices=TYPE_CHOICES, required=False, label="Type")

    # def __init__(self, *args, **kwargs):
    #     super(InstitutionFilterForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({"class": "form-control"})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "rate"]

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["rate"].widget = forms.NumberInput(attrs={
            "min": 0,
            "max": 100,
            "step": 1,
            "placeholder": "Введіть значення від 0 до 100",
            "class": "form-control"
        })
        self.fields["text"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Відгук..."
        })
        self.fields["text"].label = ""

class InsForm(forms.ModelForm):
    media = forms.ImageField(
        required=False,
        validators=[validate_image_size],
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Institution
        fields = ["name", "type", "location", "description", "media"]

    def __init__(self, *args, **kwargs):
        super(InsForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Назва..."
        })
        self.fields["name"].label = ""

        self.fields["type"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Тип..."
        })
        self.fields["type"].label = "Тип"

        self.fields["location"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Локація..."
        })
        self.fields["location"].label = ""

        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Опис..."
        })
        self.fields["description"].label = ""

        self.fields["media"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Медіа..."
        })
        self.fields["media"].label = "Медіа"

class InsFilterForm(forms.Form):
    TYPE_CHOICES = [
        ('Catering', 'Catering'),
        ('Sport', 'Sport'),
        ('Entertainment', 'Entertainment'),
        ('Education', 'Education'),
        ('Trade', 'Trade'),
        ('Beauty and health', 'Beauty and health')
    ]

    type = forms.ChoiceField(choices=TYPE_CHOICES, required=False, label="Type")

    def __init__(self, *args, **kwargs):
        super(InsFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
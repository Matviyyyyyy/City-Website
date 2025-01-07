from django import forms
from django.core.exceptions import ValidationError
from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            "class": "form-control error",
            "placeholder": "Title..."
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-control error",
            "placeholder": "Description..."
        })

    # Валідація поля title
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise ValidationError("Заголовок має містити щонайменше 5 символів.")

        forbidden_words = ['spam']
        if any(word in title.lower() for word in forbidden_words):
            raise ValidationError('Заголовок містить заборонені слова.')

        return title

    # Валідація поля description
    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 10:
            raise ValidationError("Опис має містити щонайменше 10 символів.")

        return description

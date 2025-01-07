from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils.timezone import now, make_aware
from .models import Walk

class WalkForm(forms.ModelForm):
    class Meta:
        model = Walk
        fields = ["name", "goat", "start_time", "end_time", "number_members", "type"]

        widgets = {
            'start_time': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'min': now().strftime('%Y-%m-%dT%H:%M'),
                }
            ),
            'end_time': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'min': (now() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M'),
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(WalkForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Назва..."
        })
        self.fields["name"].label = ''

        self.fields["goat"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Мета прогулянки, очікування..."
        })
        self.fields["goat"].label = ''

        self.fields["start_time"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Початковий час..."
        })
        self.fields["start_time"].label = ''

        self.fields["end_time"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Кінцевий час    ..."
        })
        self.fields["end_time"].label = ''

        self.fields["number_members"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Кількість учасників..."
        })
        self.fields["number_members"].label = 'Кількість учасників'

        self.fields["type"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Тип..."
        })
        self.fields["type"].label = 'Тип'

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time:
            # Приведення до часового поясу
            if start_time.tzinfo is None:
                start_time = make_aware(start_time)
            if end_time.tzinfo is None:
                end_time = make_aware(end_time)

            # Поточний час з урахуванням часового поясу
            current_time = now()

            if start_time < current_time:
                raise ValidationError("Start time cannot be in the past.")
            if end_time <= start_time:
                raise ValidationError("End time must be after start time.")
            if end_time < start_time + timedelta(hours=1):
                raise ValidationError("The difference between start and end time must be at least 1 hour.")
        return cleaned_data


class WalkInsEvForm(forms.ModelForm):
    class Meta:
        model = Walk
        fields = ["institution", "events"]
        widgets = {
            "institution": forms.CheckboxSelectMultiple(),
            "events": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        walk = kwargs.pop('walk', None)
        super(WalkInsEvForm, self).__init__(*args, **kwargs)

        # Встановлюємо українські назви для полів
        self.fields["institution"].label = "Заклади: "
        self.fields["events"].label = "Події"

        # Фільтруємо події за датою, якщо передано walk
        if walk and walk.start_time and walk.end_time:
            self.fields["events"].queryset = self.fields["events"].queryset.filter(
                event_date__gte=walk.start_time,
                event_date__lte=walk.end_time,
            )

        # Додаємо клас "form-control" для інших віджетів
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({"class": "form-control"})


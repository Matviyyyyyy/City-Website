from django import forms
from polls.models import Answer, Choice, Question

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        if question:
            self.fields['choice'].queryset = Choice.objects.filter(question=question)
        self.fields["choice"].widget.attrs.update({"class": "form-control"})


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['respond']

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields["respond"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Respond..."})
        self.fields["respond"].label = ""

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class": "form-control",
                "placeholder": "Питання...  ",
                })
        self.fields['text'].label = ''
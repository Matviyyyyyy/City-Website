from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from polls.models import *
from auth_system.models import *
from polls.mixing import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from polls.forms import AnswerForm, ChoiceForm, QuestionForm
from django.shortcuts import get_object_or_404

# Create your views here.


class QuestionListView(ListView):
    model = Question
    template_name = "polls/question-list.html"
    context_object_name = "questions"

class QuestionDetailView(DetailView):
    model = Question
    template_name = "polls/question-detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        answers = Answer.objects.filter(question=question).all()
        context['answer_form'] = AnswerForm(question=question)
        context['choice_form'] = ChoiceForm()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action_type')

        if action == 'answer':
            return self.answer_post(request)
        elif action == 'add_choice':
            return self.add_choice_post(request)
        else:
            return super().post(request, *args, **kwargs)

    def answer_post(self, request):
        question = self.get_object()
        answer_form = AnswerForm(request.POST, question=question)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer_qs = Answer.objects.filter(user=request.user, question=question)
            if answer_qs.exists():
                return redirect("polls:error-answer", question_id=question.pk)
            else:
                answer.save()
            return redirect('polls:question-detail', pk=question.pk)
        else:
            pass
    #
    # class CommentLikeToggle(LoginRequiredMixin, View):
    #     def post(self, request, *args, **kwargs):
    #         comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
    #         like_qs = Like.objects.filter(comment=comment, user=request.user)
    #         if like_qs.exists():
    #             like_qs.delete()
    #         else:
    #             Like.objects.create(comment=comment, user=request.user)
    #         return redirect('tasks:task-detail', pk=comment.task.pk)

    def add_choice_post(self, request):
        if not request.user.admin_or_moder():
            raise PermissionDenied
        choice_form = ChoiceForm(request.POST)
        if choice_form.is_valid():
            choice = choice_form.save(commit=False)
            choice.question = self.get_object()
            choice.save()
            return redirect('polls:question-detail', pk=choice.question.pk)
        else:
            pass

def error_answer_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, template_name="polls/error-answer.html", context={"question": question})

class QuestionCreateView(LoginRequiredMixin, UserIsAdminOrModerMixin, CreateView):
    model = Question
    template_name = "polls/question-create.html"
    context_object_name = "question"
    form_class = QuestionForm

    def get_success_url(self):
        return reverse_lazy("polls:question-detail", kwargs={'pk': self.object.pk})


class QuestionUpdateView(LoginRequiredMixin, UserIsAdminOrModerMixin, UpdateView):
    model = Question
    template_name = "polls/question-update.html"
    form_class = QuestionForm
    context_object_name = "question"

    def get_success_url(self):
        return reverse_lazy("polls:question-detail", kwargs={'pk': self.object.pk})


class QuestionDeleteView(LoginRequiredMixin, UserIsAdminOrModerMixin, DeleteView):
    model = Question
    context_object_name = "question"
    success_url = reverse_lazy("polls:question-list")


class ChoiceUpdateView(LoginRequiredMixin, UserIsAdminOrModerMixin, UpdateView):
    model = Choice
    template_name = "polls/choice-update.html"
    form_class = ChoiceForm
    context_object_name = "choice"

    def get_success_url(self):
        return reverse_lazy("polls:question-detail", kwargs={'pk': self.object.question.pk})


class ChoiceDeleteView(LoginRequiredMixin, UserIsAdminOrModerMixin, DeleteView):
    model = Choice
    context_object_name = "choice"

    def get_success_url(self):
        return reverse_lazy("polls:question-detail", kwargs={'pk': self.object.question.pk})



from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from news.mixing import *
from news.models import *
from news.forms import *
# Create your views here.



class NewListView(ListView):
    model = New
    template_name = "news/new-list.html"
    context_object_name = "news"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        type = self.request.GET.get('type', '')
        if type:
            queryset = queryset.filter(type=type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_filter_form"] = NewsFilterForm(self.request.GET)
        return context

    def get(self, request):
        super().get(request)

        if request.headers.get('x-requested-with') == "XMLHttpRequest":
            return render(request, 'news/list.html', context=self.get_context_data())

        return render(request, self.template_name, context=self.get_context_data())

class NewCreateView(LoginRequiredMixin, UserIsAdminOrModerMixin ,CreateView):
    model = New
    template_name = "news/new-create.html"
    form_class = NewForm
    success_url = reverse_lazy("news:new-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NewUpdateView(LoginRequiredMixin, UserIsAdminOrModerMixin, UpdateView):
    model = New
    template_name = "news/new-update.html"
    form_class = NewForm
    context_object_name = "new"

    def get_success_url(self):
        return reverse_lazy("news:new-list")



class NewDeleteView(LoginRequiredMixin, UserIsAdminOrModerMixin, DeleteView):
    model = New
    context_object_name = "new"
    success_url = reverse_lazy("news:new-list")
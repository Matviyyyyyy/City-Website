from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from adverts.models import *
from auth_system.models import *
from adverts.mixing import *
from adverts.forms import AdvertForm
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.


class AdvertListView(ListView):
    model = Advert
    template_name = "adverts/advert-list.html"
    context_object_name = "adverts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        adverts = Advert.objects.all()
        current_time = timezone.now()
        for advert in adverts:
            limit_time = advert.published_at + timedelta(days=advert.duration)
            if current_time >= limit_time:
                del self.request.session['advert']
                advert.delete()
        return context
class AdvertCreateView(LoginRequiredMixin, UserIsAdminOrModerMixin ,CreateView):
    model = Advert
    template_name = "adverts/advert-create.html"
    form_class = AdvertForm
    success_url = reverse_lazy("adverts:advert-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AdvertUpdateView(LoginRequiredMixin, UserIsAdminOrModerMixin, UpdateView):
    model = Advert
    template_name = "adverts/advert-update.html"
    form_class = AdvertForm
    context_object_name = "advert"

    def get_success_url(self):
        return reverse_lazy("adverts:advert-list")

class AdvertDeleteView(LoginRequiredMixin, UserIsAdminOrModerMixin, DeleteView):
    model = Advert
    template_name = "adverts/advert-delete.html"
    context_object_name = "advert"


    def get_success_url(self):
        return reverse_lazy("adverts:advert-list")




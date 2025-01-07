from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from walking.models import *
from auth_system.models import *
from walking.mixing import *
from walking.forms import WalkForm, WalkInsEvForm
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import QuerySet
from django.utils import timezone
from django.db.models import F
from django.utils import timezone

class WalkListView(LoginRequiredMixin, ListView):
    model = Walk
    template_name = "walking/walk-list.html"
    context_object_name = "walks"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        now = timezone.now()
        for walk in queryset:
            if walk.start_time < now and walk.status == "scheduled":
                print(walk.status)
                walk.status = "in_progres"
                walk.save()
            if walk.end_time <= now and walk.status == "in_progres":
                walk.status = "completed"
                print("Completed")
                walk.save()
        queryset = queryset.all()
        return queryset


class WalkDetailView(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    model = Walk
    template_name = "walking/walk-detail.html"
    context_object_name = "walk"

class WalkCreateView(LoginRequiredMixin, CreateView):
    model = Walk
    template_name = "walking/walk-create.html"
    context_object_name = "walk"
    form_class = WalkForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("walking:walk-ins-ev", kwargs={'pk': self.object.pk})
class WalkUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Walk
    template_name = "walking/walk-update.html"
    form_class = WalkForm
    context_object_name = "walk"

    def get_success_url(self):
        return reverse_lazy("walking:walk-detail", kwargs={'pk': self.object.pk})

class WalkDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Walk
    context_object_name = "walk"
    success_url = reverse_lazy("walking:walk-list")

class WalkInsEventCreate(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Walk
    template_name = "walking/walk-ins-ev.html"
    form_class = WalkInsEvForm
    context_object_name = "walk"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['walk'] = self.get_object()  # Передаємо об'єкт `walk`
        return kwargs

    def post(self, request, *args, **kwargs):
        walk = self.get_object()
        walk_ins_ev_form = WalkInsEvForm(request.POST, instance=walk)
        if walk_ins_ev_form.is_valid():
            # Нові дані з форми
            new_institutions = walk_ins_ev_form.cleaned_data.get('institution')
            new_events = walk_ins_ev_form.cleaned_data.get('events')

            # Існуючі зв’язки
            current_institutions = set(walk.institution.all())
            current_events = set(walk.events.all())

            # Додати нові зв’язки, яких немає
            institutions_to_add = set(new_institutions) - current_institutions
            events_to_add = set(new_events) - current_events

            walk.institution.add(*institutions_to_add)
            walk.events.add(*events_to_add)

            # Видалити зв’язки, яких більше немає
            institutions_to_remove = current_institutions - set(new_institutions)
            events_to_remove = current_events - set(new_events)

            walk.institution.remove(*institutions_to_remove)
            walk.events.remove(*events_to_remove)

            return redirect('walking:walk-detail', pk=walk.pk)
        else:
            pass





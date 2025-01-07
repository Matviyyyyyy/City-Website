
from django.shortcuts import render
from events.utils import CustomHTMLCalendar
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import *
from events.forms import *
from events.mixing import *
from events.models import *
from django.utils.timezone import now

def calendar_view(request, year=None, month=None):
    today = date.today()
    year = year or today.year
    month = month or today.month

    # Отримуємо події для поточного місяця
    events = Event.objects.filter(event_date__year=year, event_date__month=month)
    for e in events:
        if e.event_date < now():
            e.delete()

    # Створюємо HTML-календар з подіями
    cal = CustomHTMLCalendar(events, year, month).formatmonth(year, month)

    return render(request, 'events/calendar.html', {
        'calendar': cal,
        'events': events,
        'year': year,
        'month': month,
    })


class EventCreateView(LoginRequiredMixin, UserIsModeratorOrAdmin, CreateView):
    model = Event
    template_name = "events/add-event.html"
    form_class = EventForm
    success_url = reverse_lazy("events:calendar")

    def form_valid(self, form):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            # Перетворюємо отримані значення року, місяця і дня на об'єкт дати
            date = datetime(year, month, day)
            form.instance.event_date = date
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventDetailView(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "events/event-detail.html"

class EventUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UserIsModeratorOrAdmin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "events/event-update.html"
    def get_success_url(self):
        return reverse_lazy("events:event-detail", kwargs={'pk': self.object.pk})

class EventDeleteView(LoginRequiredMixin, UserIsOwnerMixin, UserIsModeratorOrAdmin, DeleteView):
    model = Event
    success_url = reverse_lazy("events:calendar")







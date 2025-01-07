from django.urls import path
import events.views as views

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar_by_date'),
    path('calendar/add-event/<int:year>/<int:month>/<int:day>/', views.EventCreateView.as_view(), name='add_event'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name = "event-detail"),
    path('event/update/<int:pk>/', views.EventUpdateView.as_view(), name = "event-update"),
    path('event/delete/<int:pk>/', views.EventDeleteView.as_view(), name = "event-delete"),
]

app_name="events"
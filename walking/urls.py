from django.urls import path
from walking import views

urlpatterns = [
    path("walks/", views.WalkListView.as_view(), name="walk-list"),
    path("walk/<int:pk>/", views.WalkDetailView.as_view(), name="walk-detail"),
    path("walk-create/", views.WalkCreateView.as_view(), name="walk-create"),
    path("walk-update/<int:pk>/", views.WalkUpdateView.as_view(), name="walk-update"),
    path("walk-delete/<int:pk>/", views.WalkDeleteView.as_view(), name="walk-delete"),
    path("walk-add-ins-ev/<int:pk>/", views.WalkInsEventCreate.as_view(), name="walk-ins-ev")
]

app_name = "walking"
from django.urls import path
from news import views

urlpatterns = [
    path('new-list/', views.NewListView.as_view(), name='new-list'),
    path('new-create/', views.NewCreateView.as_view(), name="new-create"),
    path('new-update/<int:pk>/', views.NewUpdateView.as_view(), name="new-update"),
    path('new-delete/<int:pk>/', views.NewDeleteView.as_view(), name="new-delete")
]

app_name = "news"
from django.urls import path
from main_page import views

urlpatterns = [
    path('', views.home_page, name="home")
]

app_name="home"
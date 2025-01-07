from django.urls import path
from adverts import views

urlpatterns = [
    path("advert-list/", views.AdvertListView.as_view(), name="advert-list"),
    path("advert-create/", views.AdvertCreateView.as_view(), name="advert-create"),
    path("advert-update/<int:pk>/", views.AdvertUpdateView.as_view(), name="advert-update"),
    path("advert-delete/<int:pk>/", views.AdvertDeleteView.as_view(), name="advert-delete")
]

app_name = "adverts"
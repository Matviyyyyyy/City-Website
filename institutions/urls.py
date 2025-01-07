from django.urls import path
from institutions import views

urlpatterns = [
    path('insts/', views.InstitutionListView.as_view(), name="ins-list"),
    path('ins/<int:pk>/', views.InstitutionDetailView.as_view(), name="ins-detail"),
    path("review-update/<int:pk>/", views.ReviewUpdateView.as_view(), name="review-update"),
    path("review-delete/<int:pk>/", views.ReviewDeleteView.as_view(), name="review-delete"),
    path("add-ins", views.InstitutionCreateView.as_view(), name="add-ins"),
    path("update-ins/<int:pk>/", views.InstitutionUpdateView.as_view(), name="update-ins"),
    path("delete-ins/<int:pk>/", views.InstitutionDeleteView.as_view(), name="delete-ins"),
    path('search/results/', views.SearchView.as_view(), name='search_view'),
    ]

app_name = "ins"
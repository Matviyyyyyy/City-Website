from django.urls import path
from auth_system import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name='login'),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("user-profile/<int:pk>/", views.UserProfileView.as_view(), name="user-profile"),
    path("user-update/<int:pk>/", views.UserUpdateView.as_view(), name="user-update"),
    path("user-list/", views.UserList.as_view(), name="user-list"),
    path("user-role/<int:pk>", views.UserRoleView.as_view(), name="user-role"),
    path("user-delete/<int:pk>", views.UserDeleteView.as_view(), name="user-delete"),

]

app_name = "auth"
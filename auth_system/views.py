from django.shortcuts import render, redirect
from auth_system.models import *
from auth_system.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.views import LoginView, LogoutView
from auth_system.forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from auth_system.mixing import *
from walking.models import *

# Create your views here.

class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True
    form_class = CustomUserAuthenticationForm


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    next_page = "home:home"


class RegisterView(CreateView):
    model = User
    template_name = "auth/register.html"
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("auth:login"))

class UserProfileView(LoginRequiredMixin, UserIsHisProfileMixin, DetailView):
    model = User
    template_name = "auth/user-profile.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        walks = Walk.objects.filter(user=user).all()
        context["walks"] = walks
        return context


class UserUpdateView(LoginRequiredMixin, UserIsHisProfileMixin, UpdateView):
    model = User
    template_name = "auth/user-update.html"
    context_object_name = "user"
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy("auth:user-profile", kwargs={'pk': self.object.pk})


class UserList(LoginRequiredMixin, UserIsAdminMixin, ListView):
    model = User
    template_name = "auth/user-list.html"
    context_object_name = "users"


class UserRoleView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    model = User
    template_name = "auth/user-role.html"
    context_object_name = "user"
    form_class = UserRoleForm
    success_url = reverse_lazy("auth:user-list")

class UserDeleteView(LoginRequiredMixin, UserIsAdminMixin, DeleteView):
    model = User
    context_object_name = "user"
    success_url = reverse_lazy("auth:user-list")


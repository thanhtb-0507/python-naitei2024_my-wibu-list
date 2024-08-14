from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from .models import Users

class ProfileView(LoginRequiredMixin, DetailView):
    model = Users
    template_name = 'profile_detail.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Users
    form_class = UserUpdateForm
    template_name = 'profile_update.html'
    context_object_name = 'user'

    success_url = reverse_lazy('profile-detail')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        # Place holder to add logic before save.
        return super().form_valid(form)

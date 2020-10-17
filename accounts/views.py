from django.shortcuts import render
from django.views import generic
from django.urls import reverse,reverse_lazy
from . import forms, models
from django.contrib.auth import get_user_model
class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"

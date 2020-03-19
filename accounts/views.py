from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView


class UserCreateView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/usercreate.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ('first_name', 'last_name', 'username', 'email')
    template_name = 'accounts/edit_user.html'
    pk_url_kwarg = 'user_pk'
    context_object_name = 'user'
    success_url = reverse_lazy('index')
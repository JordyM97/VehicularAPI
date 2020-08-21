from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Create your views here.

class UserList(ListView):
    model = get_user_model()

class UserDetail(DetailView):
    model = get_user_model()

class UserCreate(CreateView):
    model = get_user_model()

class UserUpdate(UpdateView):
    model = get_user_model()

class UserDelete(DeleteView):
    model = get_user_model()

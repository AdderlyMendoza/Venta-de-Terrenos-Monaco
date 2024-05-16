import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, CreateView,DetailView
from django.contrib.auth.models import Group
from .forms import RegisterForm, UserForm, ProfileForm, UserCreationForm
from django.views import View
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)



def welcome(request):

    if request.user.is_authenticated:

        return render(request, "usuarios/bienvenido.html")
    
    return redirect('usuarios:home')




    




from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm #We're subclassing the generic class-based view CreateView in our SignUp class. We specify using the built-in UserCreationForm
    success_url = reverse_lazy("login") #to redirect the user to the login page upon successful registration.
    template_name = "registration/signup.html"


# Create your views here.

from django.shortcuts import render, redirect
from pip import main

from .forms import RegisterForm
from main.models import Theme, Logo
from django.contrib.auth import *

# Create your views here.

def login(response):
    logo = Logo.objects.filter(pk=1).get()

def register(response):
    logo = Logo.objects.filter(pk=1).get()
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form, "logo": logo})

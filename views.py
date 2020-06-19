from django.shortcuts import render
from django.core.mail import send_mail
from .models import *


def home(request):
    exa = Example.objects.all()

    return render(request, 'home.html', {'exa': exa})

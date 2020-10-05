from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    users = User.objects.count()
    return render(request,'home.html',context={'users': users})

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    return render(request, 'registration/signup.html',context={'form':form})
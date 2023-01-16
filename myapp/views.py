from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from . import models

def home(request):
    return render(request, 'Home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def movies(request):
    return render(request, 'Movies.html')


def booking(request):
    return render(request, 'Booking.html')


def show(request):
    return render(request, 'Show.html')


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['uname']
            pass1 = request.POST['psw']
            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Bad Credentials!")
                return redirect('/')

        return render(request,"signin.html")
    else:
        return redirect('/')

def loggout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['uname']
            pass1 = request.POST['psw']
            pass2 = request.POST['psw-repeat']
            if pass1 != pass2:
                messages.error(request,"Password didn't match!")
            else:
                myuser = User.objects.create_user(username=username, password=pass1)
                myuser.is_active=True
                myuser.save()
                return redirect('/signin')
        return render(request,"signup.html")
    else:
        return redirect('/')

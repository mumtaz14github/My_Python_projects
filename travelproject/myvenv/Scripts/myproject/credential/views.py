from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def log_in(request):
    if request.method == 'POST':
        s1 = request.POST['username']
        s2 = request.POST['password']
        user = authenticate(request, username=s1, password=s2)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'log.html')


def demo(request):
    if request.method == 'POST':
        f1 = request.POST['username']  # f1,f2,f3 is any variable name
        f2 = request.POST['firstname']  # username, firstname....confirm-password is name given in register.html
        f3 = request.POST['lastname']
        f4 = request.POST['email']
        f5 = request.POST['password']
        f6 = request.POST['confirm-password']
        # me is user(variable name) User is keyword(from auth_user)
        # username, first_name, last_name are the field name of table auth_user
        if f5 == f6:
            if User.objects.filter(username=f1).exists():
                messages.info(request, "username already exists")
                return redirect('register')
            elif User.objects.filter(email=f4).exists():
                messages.info(request, "username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=f1, first_name=f2, last_name=f3, email=f4, password=f5)
                user.save()
                messages.info(request, "user created")

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')


def log_out(request):
    logout(request)
    return redirect('/')

# Create your views here.

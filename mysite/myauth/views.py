from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AuthForm
from .models import User
from django.contrib import messages


def registration_user(request):
    if request.method == "POST":
        form = AuthForm(request.POST, request.FILES)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                form.add_error('password2', "Пароли не совпадают")
            else:
                # handle_uploaded_file(request.FILES["photo"])
                form.save()
    else:
        form = AuthForm()
    context = {
        'type': "registration",
        'form': form
    }
    return render(request, "myauth/login.html", context=context)

def login_user(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        del form.fields['password2']
        del form.fields['photo']
        del form.fields['agree']
        del form.fields['username']
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["email"], password=cd["password1"])
            if user:
                login(request, user)
                return redirect('admin')
            else:
                form.add_error('email', "Пользователь не найден")
    else:
        form = AuthForm()
        del form.fields['password2']
        del form.fields['photo']
        del form.fields['agree']
        del form.fields['username']
    context = {
        'type': "login",
        'form': form
    }
    return render(request, "myauth/login.html", context=context)

def logout_user(request):
    logout(request)
    return redirect('login')
















def handle_uploaded_file(f):
    with open(f"uploads/{f}", "wb+") as file:
        for chunk in f.chunks():
            file.write(chunk)
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib import messages


def registration_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            password1 = cd.get('password1')
            password2 = cd.get('password2')
            if password1 != password2:
                form.add_error('password2', "Пароли не совпадают")
            else:
                # handle_uploaded_file(request.FILES["photo"])

                user = form.save(commit=False)  # Создаем объект пользователя без сохранения в БД
                user.username = cd["email"]  # Устанавливаем username (если требуется)
                user.set_password(cd["password1"])  # Правильно хешируем пароль
                user.save()  # Сохраняем пользователя с хешированным паролем
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "myauth/registration.html", context=context)

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["email"], password=cd["password1"])
            if user:
                login(request, user)
                return redirect('registration')
            else:
                form.add_error('email', "Пользователь не найден")
    else:
        form = LoginForm()
    context = {
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
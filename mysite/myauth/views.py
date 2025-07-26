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
            user = User.objects.get(email=cd["email"])  # Или username=cd["username"]
            user.set_password("12345")
            user.save()
            print("\n=== DEBUG AUTH ===")
            print(f"User: {user}")
            print(f"Email: {user.email}")
            print(f"DB password hash: {user.password[:50]}...")  # Выводим начало хеша

            # Проверка пароля
            input_password = cd["password1"]
            print(f"Input password: {input_password}")
            print(f"Password check: {user.check_password(input_password)}")

            if user.check_password(input_password):
                print("✅ Пароль верный")
                # Дополнительная проверка хеша
                from django.contrib.auth.hashers import identify_hasher
                try:
                    hasher = identify_hasher(user.password)
                    print(f"Hasher: {hasher.algorithm}")
                except Exception as e:
                    print(f"❌ Hash identification failed: {e}")
            else:
                print("❌ Ошибка: Неверный пароль!")
                # Проверка существования пользователя с таким паролем
                try:
                    test_user = User.objects.get(email=cd["email"], password=input_password)
                    print("⚠️ Внимание: Пароль сохранен в открытом виде!")
                except User.DoesNotExist:
                    print("Пароль в БД хранится как хеш (это нормально)")



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
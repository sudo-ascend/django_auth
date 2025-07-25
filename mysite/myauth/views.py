from django.shortcuts import render
from .forms import AuthForm
from .models import User


def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        password1 = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        if password1 != password2:
            form.add_error('password2', "Пароли не совпадают")
        else:
            form.save()
    else:
        form = AuthForm()
    context = {
        'form': form
    }
    return render(request, "myauth/login.html", context=context)

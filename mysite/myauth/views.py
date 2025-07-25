from django.shortcuts import render
from .forms import AuthForm
from .models import User


def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1 != password2:
                form.add_error('password2', "Пароли не совпадают")
            else:
                print(form.cleaned_data)
            # User.objects.create(**form.cleaned_data)
    else:
        form = AuthForm()
    context = {
        'form': form
    }
    return render(request, "myauth/login.html", context=context)

from django import forms


class AuthForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, label="Имя", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(required=True, label="email", widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(required=True, label="Пароль", widget=forms.TextInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(required=True, label="Подтвердите Пароль", widget=forms.TextInput(attrs={"class": "form-control"}))
    agree = forms.BooleanField(label="Я согласен с условиями использования", initial=True)
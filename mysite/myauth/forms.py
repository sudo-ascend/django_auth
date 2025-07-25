from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from myauth.models import User


# @deconstructible
# class RussianValidator:
#     ALLOWED_CHARS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789-_ "
#     code = "russian"
#
#     def __init__(self, message=None):
#         self.message = message if message else "Должны присутствовать только русские символы, цифрыб дефис или пробел"
#
#     def __call__(self, value, *args, **kwargs):
#         print(value)
#         for l in value:
#             print(l)
#             if not l in self.ALLOWED_CHARS:
#                 raise ValidationError(self.message, code=self.code)
#
#
# class AuthForm(forms.Form):
#     name = forms.CharField(max_length=30,
#                            required=True,
#                            label="Имя",
#                            widget=forms.TextInput(attrs={"class": "form-control"}),
#                            validators=[
#                                RussianValidator(),
#                            ])
#     email = forms.CharField(required=True, label="email", widget=forms.TextInput(attrs={"class": "form-control"}))
#     password1 = forms.CharField(min_length=8,
#                                 required=True,
#                                 label="Пароль",
#                                 widget=forms.TextInput(attrs={"class": "form-control"}),
#                                 error_messages={
#                                     "min_lenght": "Пароль не может быть менее 8 символов"
#                                 })
#     password2 = forms.CharField(required=True, label="Подтвердите Пароль", widget=forms.TextInput(attrs={"class": "form-control"}))
#     agree = forms.BooleanField(label="Я согласен с условиями использования", initial=True)


class AuthForm(forms.ModelForm):
    password2 = forms.CharField(required=True, label="Подтвердите Пароль", widget=forms.TextInput(attrs={"class": "form-control"}))
    agree = forms.BooleanField(label="Я согласен с условиями использования", initial=True)

    class Meta:
        model = User
        fields = ["name", "email", "password"]   #"__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"})
        }
        labels = {
            "name": "Имя",
            "email": "email",
            "password": "Пароль"
        }
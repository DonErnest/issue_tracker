from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    username=forms.CharField(max_length=100, required=True, label='Username')
    password=forms.CharField(max_length=100, required=True, label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='Password input', widget=forms.PasswordInput)



    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Username already exists!', code='username_already_occupied')
        except User.DoesNotExist:
            return username

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        password_check = self.cleaned_data.get('password_confirm')
        if password != password_check:
            raise ValidationError('Password does not match!', code='passwords_do_not_match')
        return self.cleaned_data
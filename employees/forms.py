from django import forms
from .models import Employee

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'department', 'password']

class LoginForm(forms.Form):
    employee_id = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

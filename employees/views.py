from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import Employee
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.password = make_password(form.cleaned_data['password'])
            employee.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'employees/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                employee = Employee.objects.get(employee_id=form.cleaned_data['employee_id'])
                if check_password(form.cleaned_data['password'], employee.password):
                    request.session['employee_id'] = employee.employee_id
                    return redirect('employee_details')
                else:
                    messages.error(request, 'Invalid credentials')
            except Employee.DoesNotExist:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'employees/login.html', {'form': form})

def employee_details(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')
    employee = Employee.objects.get(employee_id=employee_id)
    return render(request, 'employees/details.html', {'employee': employee})

def index(request):
    return render(request, 'employees/index.html')

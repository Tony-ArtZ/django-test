from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import Employee, DataEntry
from .forms import RegisterForm, LoginForm, DataEntryForm, ApprovalForm

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

def data_entry(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')
    
    employee = Employee.objects.get(employee_id=employee_id)
    
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            data_entry = form.save(commit=False)
            data_entry.employee = employee
            data_entry.save()
            messages.success(request, 'Data entry submitted successfully!')
            return redirect('my_entries')
    else:
        form = DataEntryForm()
    
    return render(request, 'employees/data_entry.html', {'form': form, 'employee': employee})

def my_entries(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')
    
    employee = Employee.objects.get(employee_id=employee_id)
    entries = DataEntry.objects.filter(employee=employee)
    
    return render(request, 'employees/my_entries.html', {'entries': entries, 'employee': employee})

def admin_panel(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')
    
    # Simple admin check - you might want to add a proper admin field to Employee model
    employee = Employee.objects.get(employee_id=employee_id)
    if employee.employee_id != 'admin':  # Assuming 'admin' is the admin employee_id
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('employee_details')
    
    pending_entries = DataEntry.objects.filter(status='pending')
    
    return render(request, 'employees/admin_panel.html', {'entries': pending_entries, 'employee': employee})

def approve_entry(request, entry_id):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')
    
    employee = Employee.objects.get(employee_id=employee_id)
    if employee.employee_id != 'admin':
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('employee_details')
    
    entry = get_object_or_404(DataEntry, id=entry_id)
    
    if request.method == 'POST':
        form = ApprovalForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, f'Entry "{entry.title}" has been updated.')
            return redirect('admin_panel')
    else:
        form = ApprovalForm(instance=entry)
    
    return render(request, 'employees/approve_entry.html', {'form': form, 'entry': entry, 'employee': employee})

def accepted_entries(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')
    
    employee = Employee.objects.get(employee_id=employee_id)
    accepted_entries = DataEntry.objects.filter(status='accepted')
    
    return render(request, 'employees/accepted_entries.html', {'entries': accepted_entries, 'employee': employee})

def index(request):
    return render(request, 'employees/index.html')

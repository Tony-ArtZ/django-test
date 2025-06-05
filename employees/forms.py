from django import forms
from .models import Employee, DataEntry

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'department', 'password']

class LoginForm(forms.Form):
    employee_id = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class DataEntryForm(forms.ModelForm):
    class Meta:
        model = DataEntry
        fields = [
            'name_of_employee',
            'eis_neis_no',
            'designation',
            'department',
            'area',
            'mac_id_of_system',
            'official_mobile_no',
            'email_id',
            'reason_for_registration',
        ]
        widgets = {
            'reason_for_registration': forms.Textarea(attrs={'rows': 3}),
        }

class ApprovalForm(forms.ModelForm):
    class Meta:
        model = DataEntry
        fields = ['status', 'admin_notes']
        widgets = {
            'admin_notes': forms.Textarea(attrs={'rows': 3}),
        }

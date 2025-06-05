from django.contrib import admin
from .models import Employee, DataEntry

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department')
    search_fields = ('employee_id', 'name', 'department')
    list_filter = ('department',)

@admin.register(DataEntry)
class DataEntryAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_employee', 'eis_neis_no', 'designation', 'department', 'area',
        'mac_id_of_system', 'official_mobile_no', 'email_id', 'status', 'created_at', 'updated_at'
    )
    list_filter = ('status', 'area', 'department', 'created_at')
    search_fields = (
        'name_of_employee', 'eis_neis_no', 'designation', 'department',
        'mac_id_of_system', 'official_mobile_no', 'email_id'
    )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                'employee', 'name_of_employee', 'eis_neis_no', 'designation', 'department',
                'area', 'mac_id_of_system', 'official_mobile_no', 'email_id', 'reason_for_registration'
            )
        }),
        ('Status', {
            'fields': ('status', 'admin_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

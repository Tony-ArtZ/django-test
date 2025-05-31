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
    list_display = ('title', 'employee', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'employee__department')
    search_fields = ('title', 'description', 'employee__name', 'employee__employee_id')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('employee', 'title', 'description', 'data_value')
        }),
        ('Status', {
            'fields': ('status', 'admin_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

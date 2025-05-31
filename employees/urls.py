from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('details/', views.employee_details, name='employee_details'),
    path('data-entry/', views.data_entry, name='data_entry'),
    path('my-entries/', views.my_entries, name='my_entries'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('approve/<int:entry_id>/', views.approve_entry, name='approve_entry'),
    path('accepted-entries/', views.accepted_entries, name='accepted_entries'),
    path('', views.index, name='index'),
]

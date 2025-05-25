from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('details/', views.employee_details, name='employee_details'),
    path('', views.index, name='index'),
]

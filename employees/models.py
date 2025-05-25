from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  # Store hashed password

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

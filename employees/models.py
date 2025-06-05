from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  # Store hashed password

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

class DataEntry(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Not Accepted'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name_of_employee = models.CharField(max_length=100)
    eis_neis_no = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    area = models.CharField(max_length=20, choices=[('HQ', 'HQ'), ('RI', 'RI')])
    mac_id_of_system = models.CharField(max_length=100)
    official_mobile_no = models.CharField(max_length=20)
    email_id = models.EmailField()
    reason_for_registration = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_of_employee} - {self.eis_neis_no} ({self.status})"

    class Meta:
        ordering = ['-created_at']

from django.db import models

# Create your models here.

#creating company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    about = models.TextField()
    type = models.CharField(max_length = 50, choices=(
        ('IT', 'IT'), 
        ('Non IT', 'Non IT'), 
        ('Mobile Phones', 'Mobile Phones')
        ))
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    about = models.TextField()
    position = models.CharField(max_length=50, choices = (
        ('Manager', 'Manager'),
        ('Software Developer', 'SD'),
        ('Project Leader', 'PL')
    ))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    



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
    


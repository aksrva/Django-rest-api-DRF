from django.db import models

# Create your models here.

# Company models
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
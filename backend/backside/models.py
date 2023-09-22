from django.db import models

# Create your models here.

class User_details(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(default='example@gamil.com')
    dateAndTime = models.DateTimeField(auto_now=True)

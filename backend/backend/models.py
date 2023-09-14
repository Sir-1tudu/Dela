from django.db import models

class User_data(models.Model):
    user_fname = models.CharField(max_length=50)
    user_lname = models.CharField(max_length=50)
    user_image = models.ImageField()
    user_email = models.EmailField()
    user_age = models.IntegerField()
    user_dob = models.IntegerField()
    user_phone_no = models.IntegerField()
    user_gender = models.Choices()
    user_descriptions = models.CharField()
    data_time = models.DateTimeField()
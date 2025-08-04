from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    email= models.EmailField(max_length=255, blank=True)
    phone_number= models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
        

class MenuItem(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    price= models.DecimalFirld(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name
        
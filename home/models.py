from django.db import models

# Create your models here.
class RestaurantName(models.Model):
    name= models.CharField(max_length=100, unique=True, default="My Awesome Restaurant")
    def __str__(self):
        return self.name


class RestaurantName(models.Model):
    name= models.CharField(max_length=100, unique=True, default="My Awesome Restaurant")

    def __str__(self):
        return self.name
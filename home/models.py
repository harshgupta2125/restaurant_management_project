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


def about_view(request):
    context={
        'restaurant_description':(
            "Established in 2023. The Django Diner is a culinary haven"
            "dedicated to serving delicious, locally-sourced comfor food."
            "Our mission is to create a welcoming atmospher where friends"

        ),

    }
    return render (request, 'templates/about.html', context)

    
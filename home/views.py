from django.shortcuts import render
from .models import MenuItem
# Create your views here.

def menu_page_view(request):
    menu_items= MenuItem.objects.all()
    context= {
        'menu_items': menu_items
    }

    return render(request, 'menu_page.html', context)
    


def homepage_view(request):
    restaurant_name= None
    try:
        restaurant_name_obj= RestaurantName.objects.first()
        if restaurant_name_obj:
            restaurant_name= restaurant_name_obj.name 

    except RestaurantName.DoesNotExist:
        pass

    if not restaurant_name:
        restaurant_name= getattr(setting, 'RESTAURANT_NAME', 'Default Diner')

    context={
        'restaurant_name': restaurant_name,
    }

    return render (request, 'templates/home.html', context)
    
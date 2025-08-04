from django.shortcuts import render
from .models import MenuItem
# Create your views here.

def menu_page_view(request):
    menu_items= MenuItem.objects.all()
    context= {
        'menu_items': menu_items
    }

    return render(request, 'menu_page.html', context)
    
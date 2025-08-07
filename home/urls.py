from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage_view, about_view),
    path('about/', about_view, name='about'),
    
]
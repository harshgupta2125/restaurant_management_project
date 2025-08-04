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
        
class Order(models.Model):
    customer= models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount= models.DecimalField(max_digits=8, decimal_places
    =2, default=0.00)
    items= models.ManyToManyField(MenuItem, through='OrderItem')
    
    ORDER_STATUS_CHOICES=[
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('OUT_FOR_DELIVERY', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    status= models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='PENDING')
    created_at= models.DateTime(auto_now_add= True)
    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item= models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for order #{self.order.id}"
        


class ContactSubmission(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    message= models.TextField()
    submitted_at= models.DateTime(auto_now_add=True)

    def __str__(self):
        return f "Contact form submission from {self.name} on {self.submitted_at.strftime('%Y-%m-%d')}"


class RestrauntSettings(models.Model):
    name= models.CharField(max_length=255, default= 'My Awesome Restraunt')

    def save(self, *args, **kwargs):
        if RestrauntSettings.objects.exists() and not self.pk:
            existing_instance= RestrauntSettings.objects.first()
            self.pk= existing_instance.pk
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
    def __str__(self):
        return self.name
        
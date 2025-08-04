from django.contrib import admin
from .models import MenuItem, Order, OrderItems
# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields= ('name',)

class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    fields=('menu_item', 'quantity',)
    extra=1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= ('id', 'customer', 'status', 'total_amount', 'created_at')
    readonly_fields= ('total_amount', 'created_at')
    inline= [OrderItemsInline]

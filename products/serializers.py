from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MenuItemSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=255)
    description= serializers.CharField()
    price= serializers.DecimalField(max_length=5, decimal_places=2)
    
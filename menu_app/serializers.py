# menu/serializers.py
from rest_framework import serializers
from .models import Menu, Order

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'image', 'price', 'rating']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            request = self.context.get('request')
            representation['image'] = request.build_absolute_uri(f'/static{instance.image.url}')
        return representation

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'price']

class OrderSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        if data['payment_method'] == 'transfer' and 'payment_proof' not in data:
            raise serializers.ValidationError("Payment proof is required for transfer method.")
        if data['payment_method'] == 'cash' and 'payment_proof' in data:
            raise serializers.ValidationError("Payment proof should not be provided for cash method.")
        return data

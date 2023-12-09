# menu/serializers.py
from rest_framework import serializers
from .models import Menu

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

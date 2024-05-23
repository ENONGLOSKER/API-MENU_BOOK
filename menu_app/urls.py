# menu/urls.py
from django.urls import path
from .views import menu_list, menu_detail, menu_list, order_detail, order_list

urlpatterns = [
    path('menu/', menu_list, name='menu-list-create'),
    path('menu/<int:pk>/', menu_detail, name='menu-detail'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:pk>/', order_detail, name='order_detai')
]

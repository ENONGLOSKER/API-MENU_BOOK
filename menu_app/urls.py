# menu/urls.py
from django.urls import path
from .views import menu_list, menu_detail, menu_list

urlpatterns = [
    path('menu/', menu_list, name='menu-list-create'),
    path('menu/<int:pk>/', menu_detail, name='menu-detail'),
]

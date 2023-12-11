from django.urls import path
from .views import wine, about, menu

urlpatterns = [
    path('', wine, name='wine'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
]
from django.urls import path
from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/', views.cart_add, name='cart_add'),
    path('card_change/', views.cart_change, name='cart_change'),
    path('cart_remove', views.cart_remove, name='cart_remove')
    
    
]
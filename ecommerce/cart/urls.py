from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_details, name='cartdetails'),
    path('add/<int:product_id>', views.add_cart, name='add'),
    path('reduce/<int:product_id>', views.reduce_quantity, name='reduce'),
    path('delete/<int:product_id>', views.remove_product, name='delete'),
]
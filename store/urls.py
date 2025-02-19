from django.urls import path
from .views import *

urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-item/', updateItem, name='updateItem'),
    path('process-order/', processOrder, name="process-order"),
]
from django.urls import path
from shop import views



urlpatterns = [
    path('', views.Home.as_view(),
    name='home'),
    
    path('cart/', views.Cart.as_view(),
    name='cart'),
    
    path('single/<product_id>', views.Single.as_view(), 
    name='single')
    
]

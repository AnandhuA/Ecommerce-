from django.urls import path
from login import views



urlpatterns = [
    
    path('sign_up',views.Sign_Up.as_view(),name='sign_up'),
    
    path('login',views.Login.as_view(),name='login'),
    
    path('logout',views.Logout.as_view(),name='logout'),
    
    path('buynow/<product_id>',views.BuyNow.as_view(),name='buynow'),
    
    path('checkout',views.CheckOut.as_view(),name='checkout'),
    
    path('account', views.Account.as_view(),name='account')
    
]

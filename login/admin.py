from django.contrib import admin
from login.models import order



class AdminOrders(admin.ModelAdmin):
  list_display = ['product_name']


# Register your models here.

admin.site.register(order, AdminOrders )
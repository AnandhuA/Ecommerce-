from django.contrib import admin
from shop.models import products,category


class AdminProduct(admin.ModelAdmin):
  list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
  list_display = ['name']


# Register your models here.

admin.site.register(products, AdminProduct)
admin.site.register(category, AdminCategory)
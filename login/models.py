from django.db import models
from login.form import custom_user
from shop.models import products
import datetime

# Create your models here.

class order(models.Model):
  
  products = models.ForeignKey(products, on_delete = models.CASCADE)
  product_name = models.CharField(max_length=50,default = "unknown")
  quantity = models.IntegerField(default = 1 )
  price = models.IntegerField()
  customer = models.CharField(max_length=50, default = "unknown")
  address = models.CharField(max_length = 150, default = "unknown")
  place = models.CharField(max_length = 100, default = "unknown")
  city = models.CharField(max_length = 50, default = "unknown")
  phone = models.CharField(max_length = 10)
  date = models.DateField(default = datetime.datetime.today)
  
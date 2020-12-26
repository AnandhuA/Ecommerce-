from django.db import models


# Create your models here.


#category model
class category(models.Model):
  
    name = models.CharField(max_length = 20)
     
#show category name     
    def __str__(self):
      return self.name
      
      
#product model     

class products (models.Model):
  
    name = models.CharField(max_length = 50)
    
    category = models.ForeignKey(category, on_delete = models.CASCADE, default = 1)
      
    price = models.IntegerField(default= 0)
      
    description = models.CharField(max_length = 300)
      
    image = models.ImageField(upload_to ='upload/upload_images')
      
      

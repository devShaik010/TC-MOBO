from django.db import models
from .categories import Categories
import datetime

# this is for product card items 
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    discount = models.IntegerField(default=0)
    desc = models.CharField(max_length=40)
    image = models.ImageField(upload_to="Uploads/product")
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE, default=1)
    date = models.DateField(default=datetime.datetime.today)


   #storing data in function 
    @staticmethod
    def get_all():
        return Product.objects.all().order_by('-date')

    @staticmethod
    def get_all_filter(category_1):
        if category_1:
         return Product.objects.filter(categories = category_1).order_by('-date')  
        else:
         return Product.get_all()  
    
    @staticmethod
    def get_product_by_id(ids):
       return Product.objects.filter(id__in = ids ).order_by('-date')
from django.db import models
from .b_catogeries import B_categories
import datetime


class Book(models.Model):
    date = models.DateField(default=datetime.datetime.today)
    owner_name = models.CharField(max_length=40)
    contact = models.CharField(max_length=15)
    model = models.CharField(max_length=40)
    brand = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=150)
    image = models.ImageField(upload_to="Uploads\Books")
    image_1 = models.ImageField(upload_to="Uploads\Books")
    image_2 = models.ImageField(upload_to="Uploads\Books")
    b_categories = models.ForeignKey(B_categories,on_delete=models.CASCADE, default=1)

   #storing data in function 
    @staticmethod
    def get_all():
        return Book.objects.all()

    @staticmethod
    def get_all_filter(b_category):
        if b_category:
            return Book.objects.filter(b_categories = b_category )    
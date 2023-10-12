from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="Uploads/product")

    @staticmethod
    def all_catogaries():
        return Categories.objects.all()
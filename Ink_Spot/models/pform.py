from django.db import models

# this is for product card items 
class Pform(models.Model):
    url = models.CharField(max_length=400,default="empty")
   

   #storing data in function 
    @staticmethod
    def get_all():
        return Pform.objects.all()

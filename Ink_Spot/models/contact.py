from django.db import models

# this is for product card items 
class Contact(models.Model):
    offcial_phone = models.CharField(max_length=20,default=7330012300)
    email = models.EmailField()
    
    

   #storing data in function 
    @staticmethod
    def get_all():
        return Contact.objects.all()
  
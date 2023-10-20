from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
# this is for product card items 
class Contact(models.Model):
    offcial_phone = models.CharField(max_length=20,default=7330012300)
    email = models.EmailField()

    image = models.ImageField(upload_to="Uploads/Books",default="Uploads/Books/1.jpg")
    image_1 = models.ImageField(upload_to="Uploads/Books",default="Uploads/Books/1.jpg")
    image_2 = models.ImageField(upload_to="Uploads/Books",default="Uploads/Books/1.jpg")
    
    

   #storing data in function 
    @staticmethod
    def get_all():
        return Contact.objects.all()
  
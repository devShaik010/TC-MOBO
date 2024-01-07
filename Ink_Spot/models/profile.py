from django.db import models
from .profilecat import Profilecat

# this is for Profile card items 
class Profile(models.Model):
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    services = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="statics/Uploads/profile")
    categories = models.ForeignKey(Profilecat,on_delete=models.CASCADE, default=1)
    status = models.BooleanField(default=False)


   #storing data in function 
    @staticmethod
    def get_all():
        return Profile.objects.all()

    @staticmethod
    def get_all_filter(category_1):
        if category_1:
         return Profile.objects.filter(categories = category_1)  
        else:
         return Profile.get_all()  
    
    @staticmethod
    def get_profile_by_id(ids):
       return Profile.objects.filter(id__in = ids )
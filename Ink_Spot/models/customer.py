from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    area = models.CharField(max_length=300,default='Hyderabad')
    password = models.CharField(max_length=500  )

    def register(self):
        self.save()
    
    def isExist(self):
        if Customer.objects.filter(email  = self.email):
            return True
        return False 

    def isname(self):
        if Customer.objects.filter(name  = self.name):
            return True
        return False 

    def isnumber(self):
        if Customer.objects.filter(phone  = self.phone):
            return True
        return False 
    
    @staticmethod
    def get_cutomer_by_email(email):
        return Customer.objects.get(email = email)
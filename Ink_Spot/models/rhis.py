from .customer import Customer
from django.db import models
import datetime
from .order import Order

class Rhis(models.Model):  
    customer  = models.ForeignKey(Customer, on_delete=models.CASCADE)
    problem = models.CharField(max_length=100,default='none',blank=True)
    company = models.CharField(max_length=100,default='none',blank=True)
    modal = models.CharField(max_length=100,default='none',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)



    def request_history_save(self):
        self.save()
        
    @staticmethod
    def get_history_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)


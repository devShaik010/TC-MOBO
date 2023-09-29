from django.db import models

class Profilecat(models.Model):
    name = models.CharField(max_length=20)


    @staticmethod
    def all_catogaries():
        return Profilecat.objects.all()
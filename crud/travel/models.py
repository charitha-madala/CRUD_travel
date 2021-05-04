from django.db import models

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    destination= models.CharField(max_length=10)
    date = models. DateField(auto_now=False, auto_now_add=False)
    price = models.CharField(max_length=15,default="")
    rt_pcr = models.BooleanField()
    
    



# Create your models here.
from django.db import models
from datetime import date 
from django.utils import timezone 

class custumer(models.Model):
    id_custumer = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    telephone = models.IntegerField ()
    checkin = models.TimeField(default = timezone.now)
    checkout = models.TimeField(null=True, blank=True)



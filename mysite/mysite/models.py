from django.db import models
class salservercon(models.Model):
    employeeID=models.IntegerField(max_length=100)
    LastName=models.CharField(max_length=100)
    FirstName =models.CharField(max_length=100)
    City= models.CharField(max_length=100)
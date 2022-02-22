from django.db import models


# Create your models here.

class Contact(models.Model):

    firstName=models.CharField(max_length=15)

    lastName=models.CharField(max_length=15)

    email=models.CharField( max_length=50)

    address=models.CharField(max_length=100)

    zipcode=models.CharField(max_length=5)

    phone=models.CharField(max_length=30)

    date=models.DateField()
 








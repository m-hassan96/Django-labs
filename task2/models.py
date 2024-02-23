from django.db import models

# Create your models here.

class Product(models.Model):
        name=models.CharField(max_length=50,null=True)
        price=models.IntegerField(null=True)
        color=models.CharField(max_length=50,null=True)
        category=models.CharField(max_length=50,null=True)
        image=models.CharField(max_length=100,null=True)
        # createdate=models.DateTimeField(auto_now_add=True)#
        # updatedate=models.DateTimeField(auto_now=True)


class Category(models.Model):
        cName=models.CharField(max_length=50,null=True)
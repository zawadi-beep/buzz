from django.db import models

# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    YOB = models.DateField(null = True)

    def __str__(self):
        return self.fullname


class products(models.Model):
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product

from django.db import models

# Create your models here.

class UserModel1(models.Model):
    sign=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default='Na')
    username=models.CharField(max_length=30,default='Na',unique=True)
    email=models.EmailField(null=False)
    password=models.CharField(max_length=8,unique=True)



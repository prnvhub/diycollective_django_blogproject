from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify, title
from datetime import datetime,date
from django.conf import settings

# Create your models here.

class post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=250,blank=False)
    body=models.TextField(null=True,blank=False)
    img=models.ImageField(upload_to="images/",null=True,blank=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
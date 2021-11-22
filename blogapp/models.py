from django.db import models
from django.template.defaultfilters import slugify, title
from datetime import datetime,date

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=100)
    body=models.TextField()
    img=models.ImageField(upload_to="images")
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
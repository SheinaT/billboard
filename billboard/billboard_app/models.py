from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Billboard(models.Model):
    pub_date=models.DateTimeField('date posted', default=timezone.now())
    title=models.CharField(max_length=200)
    text= models.CharField(max_length=1000)
    author= models.CharField(max_length=100)




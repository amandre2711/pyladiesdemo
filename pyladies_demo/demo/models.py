# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here
class Inventory(models.Model):
    count = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    #hold off on this, show as Inventorys and then come back and code
    class Meta:
    	verbose_name_plural = "Inventory"

   

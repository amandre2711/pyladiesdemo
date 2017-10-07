# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pyladies_demo.demo.models import *

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    
    list_display = ['count', 'name', 'description', 'price', 'cost', 'available', 'profit_margin']
    #pause on profit margin
    #pause on color formatting
    def profit_margin(self, obj):
    	profit = obj.price - obj.cost
    	if profit >= 0:
    		return '<div align="right" style="background-color:#b3ffb3;"><b>' + "%.2f" % profit + '</b></div>'
    	else:
    		return '<div align="right"style="background-color:#ff9999;"><b>' + "%.2f" % profit + '</b></div>'

    profit_margin.allow_tags = True
    
admin.site.register(Inventory, InventoryAdmin)


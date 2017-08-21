# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from .models import Price, PriceLadoga, PriceNekrasova, PricePupish
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class PriceResource(resources.ModelResource):

	class Meta():
		model = Price
		exclude = ['']

class PriceAdmin(ImportExportModelAdmin):
    resource_class = PriceResource
    list_display = ['volume']

admin.site.register(Price, PriceAdmin)

class PriceLadogaAdmin(admin.ModelAdmin):
	list_display = ['pricedate_ladoga', 'petrol95_ladoga', 'petrol92_ladoga', 'diesel_ladoga']

admin.site.register(PriceLadoga, PriceLadogaAdmin)

class PriceNekrasovaAdmin(admin.ModelAdmin):
	list_display = ['pricedate_nekrasova', 'petrol95_nekrasova', 'petrol92_nekrasova', 'diesel_nekrasova']

admin.site.register(PriceNekrasova, PriceNekrasovaAdmin)

class PricePupishAdmin(admin.ModelAdmin):
	list_display = ['pricedate_pupish', 'petrol95_pupish', 'petrol92_pupish', 'diesel_pupish']

admin.site.register(PricePupish, PricePupishAdmin)
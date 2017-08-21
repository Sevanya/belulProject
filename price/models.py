# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Price(models.Model):
	volume = models.CharField(max_length=30,blank=True, verbose_name='Объем')
	petrol_95 = models.FloatField(null=True,blank=True, verbose_name='Бензин 95')
	petrol_92 = models.FloatField(null=True,blank=True, verbose_name='Бензин 92')
	diesel = models.FloatField(null=True,blank=True, verbose_name='Дизель')
	price_date = models.CharField(max_length=20, blank=True, verbose_name='Дата', default=True)

	class Meta():
		verbose_name = 'Оптовые цены'
		verbose_name_plural = 'Оптовые прайс-листы'

class PriceLadoga(models.Model):
	petrol95_ladoga = models.FloatField(null=True, blank=True, verbose_name='Ладога Бензин 95')
	petrol92_ladoga = models.FloatField(null=True, blank=True, verbose_name='Ладога Бензин 92')
	diesel_ladoga = models.FloatField(null=True, blank=True, verbose_name='Ладога Дизель')
	pricedate_ladoga = models.DateField(verbose_name='Дата')

	class Meta():
		db_table = 'price_ladoga'
		verbose_name = 'Прайс Ладога'
		verbose_name_plural = 'Прайс-листы Ладога'

class PriceNekrasova(models.Model):
	petrol95_nekrasova = models.FloatField(null=True, blank=True, verbose_name='Некрасова Бензин 95')
	petrol92_nekrasova = models.FloatField(null=True, blank=True, verbose_name='Некрасова Бензин 92')
	diesel_nekrasova = models.FloatField(null=True, blank=True, verbose_name='Некрасова Дизель')
	pricedate_nekrasova = models.DateField(verbose_name='Дата')

	class Meta():
		db_table = 'price_nekrasova'
		verbose_name = 'Прайс Некрасова'
		verbose_name_plural = 'Прайс-листы Некрасова'

class PricePupish(models.Model):
	petrol95_pupish = models.FloatField(null=True, blank=True, verbose_name='Пупышево Бензин 95')
	petrol92_pupish = models.FloatField(null=True, blank=True, verbose_name='Пупышево Бензин 92')
	diesel_pupish = models.FloatField(null=True, blank=True, verbose_name='Пупышево Дизель')
	pricedate_pupish = models.DateField(verbose_name='Дата')

	class Meta():
		db_table = 'price_pupish'
		verbose_name = 'Прайс Ладога'
		verbose_name_plural = 'Прайс-листы Пупышево'




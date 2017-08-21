# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Connect(models.Model):
	connect_firstname = models.CharField(max_length=15, verbose_name = 'Имя')
	connect_lastname = models.CharField(max_length=15, verbose_name = 'Фамилия')
	connect_mail = models.EmailField(max_length=120, verbose_name = 'E-mail')
	connect_phonenumber = models.IntegerField(verbose_name = 'Номер телефона')
	connect_text = models.TextField(blank=True, verbose_name = 'Сообщение')

	class Meta():
		db_table = 'connect'
		verbose_name = 'Обратная связь'
		verbose_name_plural = 'Обращения от пользователей'

	def __unicode__(self):
		return "%s %s" % (self.connect_lastname, self.connect_firstname)

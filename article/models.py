# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor.widgets import CKEditorWidget


# Create your models here.
class Article(models.Model):
	article_title = models.CharField(max_length=200, verbose_name='Название статьи')
	article_date = models.DateField(verbose_name='Дата публикации')
	article_description = models.TextField(blank=True, default='...', max_length=600)
	article_text = RichTextUploadingField()
	article_namesource = models.CharField(max_length=70, verbose_name='Название источника', default='Oilexp.ru')
	article_source = models.CharField(max_length=200, blank=True, verbose_name='Ссылка на источник')

	class Meta():
		db_table = 'article'
		ordering = ['-article_date']
		verbose_name = 'Новости'
		verbose_name_plural = 'Статьи'

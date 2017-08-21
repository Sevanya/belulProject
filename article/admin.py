# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article
from django.contrib.flatpages.models import FlatPage

# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['article_title', 'article_date']
	search_fields = ['article_title', 'article_date']
	list_filter = ['article_date']
	ordering = ['article_date']

class FlatpageForm(FlatpageFormOld):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		exclude = ['']
		model = FlatPage # this is not automatically inherited from FlatpageFormOld


class FlatPageAdmin(FlatPageAdminOld):
	form = FlatpageForm


# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Article, ArticleAdmin)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class ConnectAdmin(admin.ModelAdmin):
	list_display = ['connect_lastname', 'connect_firstname', 'connect_phonenumber']
	search_fields = ['connect_lastname','connect_firstname','connect_phonenumber']

admin.site.register(Connect, ConnectAdmin)

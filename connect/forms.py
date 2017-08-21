# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import *

class ConnectForm(forms.ModelForm):
	class Meta():
		model = Connect
		exclude = ['']
		error_messages = {'connect_mail': {'required': 'Введите E-mail в формате example@example.com'}, 'connect_phonenumber': {'required':'Введите номер в формате 79211234567 или 8121234567'}}
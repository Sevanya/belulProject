# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_auto_20170526_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='connect_mail',
            field=models.EmailField(help_text='fuckingNigga!', max_length=120, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='connect',
            name='connect_text',
            field=models.TextField(blank=True, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435'),
        ),
    ]

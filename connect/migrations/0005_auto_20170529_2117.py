# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_auto_20170529_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='connect_phonenumber',
            field=models.IntegerField(max_length=11, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
    ]

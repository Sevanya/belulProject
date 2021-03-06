# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 14:38
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u044c\u0438')),
                ('article_date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('article_namesource', models.CharField(default='Oilexp.ru', max_length=70, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430')),
                ('article_source', models.CharField(blank=True, max_length=200, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a')),
            ],
            options={
                'ordering': ['-article_date'],
                'db_table': 'article',
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
        ),
    ]

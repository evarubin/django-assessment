# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_auto_20170811_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveytranslation',
            name='slug',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-27 01:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20181227_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='writerEmail',
        ),
    ]

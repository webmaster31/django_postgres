# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-25 00:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0021_auto_20161024_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]

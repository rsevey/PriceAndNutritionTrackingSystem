# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantity',
            old_name='quantity',
            new_name='amount',
        ),
    ]

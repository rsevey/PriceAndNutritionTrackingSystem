# Generated by Django 2.0.1 on 2018-03-12 09:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20180201_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryfood',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='WARNING: Only for once-off items! Cost and nutrients will be overwritten by ingredients or recipes', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

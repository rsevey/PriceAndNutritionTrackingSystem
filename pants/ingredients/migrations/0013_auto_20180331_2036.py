# Generated by Django 2.0.1 on 2018-03-31 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0012_ingredient_serving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='serving',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Optional grams per serving. WARNING Nutrients are still entered per-KG.', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

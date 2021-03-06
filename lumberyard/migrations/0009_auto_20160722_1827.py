# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 18:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import lumberyard.models


class Migration(migrations.Migration):

    dependencies = [
        ('lumberyard', '0008_auto_20160722_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='date_awarded',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='date_delivery',
            field=models.DateField(default=lumberyard.models.date_plus_30, verbose_name='date delivery'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='date_pitch',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]

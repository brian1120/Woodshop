# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumberyard', '0011_remove_jobs_job_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_active',
            field=models.BooleanField(default=True),
        ),
    ]

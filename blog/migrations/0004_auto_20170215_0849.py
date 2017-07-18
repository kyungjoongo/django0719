# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='test',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-12 13:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billboard_app', '0002_auto_20190112_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billboard',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 12, 13, 35, 14, 390899, tzinfo=utc), verbose_name='date posted'),
        ),
    ]
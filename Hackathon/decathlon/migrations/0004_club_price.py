# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decathlon', '0003_auto_20181103_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

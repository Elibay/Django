# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decathlon', '0006_auto_20181103_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='type_of',
            new_name='typeOf',
        ),
    ]

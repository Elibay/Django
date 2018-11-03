# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('photos', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=250)),
                ('size', models.CharField(max_length=5)),
                ('decopoint', models.IntegerField(default=0)),
                ('photos', models.CharField(max_length=10000)),
                ('clubs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='decathlon.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Marathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('date', models.CharField(max_length=1000)),
                ('photos', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('size', models.CharField(max_length=10)),
                ('price', models.IntegerField(default=0)),
                ('photos', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='decathlon.Product'),
        ),
    ]

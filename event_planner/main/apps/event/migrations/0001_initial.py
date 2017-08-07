# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('goer', models.ManyToManyField(related_name='goer', to='login.User')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maker', to='login.User')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 03:15
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='createdby',
            field=models.ForeignKey(default=django.contrib.auth.models.User, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

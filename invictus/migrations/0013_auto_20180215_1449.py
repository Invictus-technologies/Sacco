# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-15 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invictus', '0012_auto_20180215_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='password1',
            new_name='set_password',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-14 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invictus', '0005_uploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_members',
            name='member_no',
            field=models.IntegerField(),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0002_workcode_workcode_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='workcode',
            name='workcode_serial',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_rotation', '0002_auto_20160927_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turn',
            old_name='date_removed',
            new_name='date_canceled',
        ),
    ]
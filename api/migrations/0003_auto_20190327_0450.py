# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190327_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='codname',
            new_name='codename',
        ),
    ]

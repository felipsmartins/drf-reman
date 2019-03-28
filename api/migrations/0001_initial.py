# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codname', models.CharField(blank=True, max_length=30)),
                ('version', models.CharField(max_length=60)),
                ('date', models.DateTimeField(verbose_name='release_date')),
            ],
        ),
    ]

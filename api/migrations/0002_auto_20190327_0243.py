# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppPublishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='pub_date')),
            ],
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ('-release_date',), 'verbose_name_plural': 'releases'},
        ),
        migrations.RenameField(
            model_name='release',
            old_name='date',
            new_name='release_date',
        ),
        migrations.AlterField(
            model_name='release',
            name='version',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='apppublishing',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Release'),
        ),
        migrations.AddField(
            model_name='apppublishing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Customer'),
        ),
    ]
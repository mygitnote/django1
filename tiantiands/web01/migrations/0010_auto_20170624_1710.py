# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web01', '0009_auto_20170623_1459'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recent_views',
            unique_together=set([('pid', 'uid')]),
        ),
    ]

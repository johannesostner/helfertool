# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0004_helpersgifts_got_shirt'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='deservedgiftset',
            unique_together=set([('helper', 'gift_set', 'shift')]),
        ),
    ]
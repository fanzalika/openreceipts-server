# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 20:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_receiptscan_parsed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiptscan',
            old_name='parsed',
            new_name='full_text',
        ),
    ]

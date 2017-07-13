# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170430_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='physicianID',
            field=models.ForeignKey(db_column=b'doctorID_id', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Physician'),
        ),
    ]
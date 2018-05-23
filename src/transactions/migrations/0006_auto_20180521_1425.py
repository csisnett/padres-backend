# Generated by Django 2.0.1 on 2018-05-21 14:25

import annoying.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20180521_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ownership',
            field=annoying.fields.AutoOneToOneField(blank=True, null=True, on_delete='PROTECT', related_name='companies', to='transactions.Owner'),
        ),
    ]
# Generated by Django 2.0.1 on 2018-05-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_auto_20180521_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ownership',
            field=models.OneToOneField(null=True, on_delete='PROTECT', related_name='companies', to='transactions.Owner'),
        ),
    ]
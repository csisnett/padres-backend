# Generated by Django 2.0.1 on 2018-05-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ownership',
            field=models.OneToOneField(blank=True, null=True, on_delete='PROTECT', related_name='companies', to='transactions.Owner'),
        ),
    ]

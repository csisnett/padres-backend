# Generated by Django 2.0.1 on 2018-05-21 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0002_auto_20180504_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legalcase',
            old_name='event',
            new_name='events',
        ),
    ]
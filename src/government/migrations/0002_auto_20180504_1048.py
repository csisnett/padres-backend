# Generated by Django 2.0.1 on 2018-05-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalcase',
            name='event',
            field=models.ManyToManyField(blank=True, to='padres.Event'),
        ),
        migrations.AlterField(
            model_name='legalcase',
            name='people',
            field=models.ManyToManyField(blank=True, to='padres.Person'),
        ),
    ]
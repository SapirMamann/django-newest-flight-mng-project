# Generated by Django 4.1.6 on 2023-02-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airlinecompany',
            name='name',
            field=models.CharField(default=None, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='name',
            field=models.CharField(default=None, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]

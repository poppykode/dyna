# Generated by Django 2.1.5 on 2019-02-22 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20190220_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanofthematch',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 22, 11, 31, 25, 166290)),
        ),
        migrations.AlterField(
            model_name='loyalty',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 22, 11, 31, 25, 168289)),
        ),
        migrations.AlterField(
            model_name='manofthematch',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 11, 31, 25, 167290)),
        ),
        migrations.AlterField(
            model_name='momementofthematch',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 11, 31, 25, 169288)),
        ),
        migrations.AlterField(
            model_name='travelwiththeteam',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 11, 31, 25, 168289)),
        ),
    ]

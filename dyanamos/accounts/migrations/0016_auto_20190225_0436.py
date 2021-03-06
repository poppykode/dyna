# Generated by Django 2.1.5 on 2019-02-25 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20190222_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fanofthematch',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 25, 4, 35, 59, 325694)),
        ),
        migrations.AlterField(
            model_name='loyalty',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 25, 4, 35, 59, 328692)),
        ),
        migrations.AlterField(
            model_name='manofthematch',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 4, 35, 59, 326694)),
        ),
        migrations.AlterField(
            model_name='momementofthematch',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 4, 35, 59, 329691)),
        ),
        migrations.AlterField(
            model_name='travelwiththeteam',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 4, 35, 59, 327692)),
        ),
    ]

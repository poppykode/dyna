# Generated by Django 2.1.5 on 2019-02-20 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190220_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanofthematch',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 20, 14, 25, 3, 980916)),
        ),
        migrations.AlterField(
            model_name='loyalty',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 20, 14, 25, 3, 982915)),
        ),
        migrations.AlterField(
            model_name='travelwiththeteam',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 14, 25, 3, 981915)),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-25 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20190225_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sub_expiration_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='fanofthematch',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 25, 11, 48, 39, 245236)),
        ),
        migrations.AlterField(
            model_name='loyalty',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 25, 11, 48, 39, 260861)),
        ),
        migrations.AlterField(
            model_name='manofthematch',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 11, 48, 39, 245236)),
        ),
        migrations.AlterField(
            model_name='momementofthematch',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 11, 48, 39, 260861)),
        ),
        migrations.AlterField(
            model_name='travelwiththeteam',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 11, 48, 39, 245236)),
        ),
    ]
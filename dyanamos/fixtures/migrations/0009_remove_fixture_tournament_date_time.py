# Generated by Django 2.1.5 on 2019-02-19 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0008_auto_20190219_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='tournament_date_time',
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20190215_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentteam',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='currentteam',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]

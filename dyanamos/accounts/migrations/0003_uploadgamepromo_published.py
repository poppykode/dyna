# Generated by Django 2.1.5 on 2019-02-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_uploadgamepromo'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadgamepromo',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
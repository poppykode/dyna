# Generated by Django 2.1.5 on 2019-02-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='tournament',
            field=models.CharField(blank=True, default='n/a', max_length=255),
        ),
    ]

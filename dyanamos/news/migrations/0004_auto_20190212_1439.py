# Generated by Django 2.1.5 on 2019-02-12 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190212_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['date_created'], 'verbose_name_plural': 'News'},
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0003_log'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['points']},
        ),
        migrations.AlterField(
            model_name='log',
            name='points',
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0006_auto_20190216_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='home_or_away',
            field=models.CharField(choices=[('Home', 'Home'), ('Away', 'Away')], max_length=20),
        ),
    ]

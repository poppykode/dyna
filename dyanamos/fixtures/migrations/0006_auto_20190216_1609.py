# Generated by Django 2.1.5 on 2019-02-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0005_auto_20190212_2049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_or_away',
            field=models.CharField(choices=[('Home', 'Home'), ('Away', 'Away')], default='n/a', max_length=20),
        ),
    ]
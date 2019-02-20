# Generated by Django 2.1.5 on 2019-02-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20190215_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentteam',
            name='surname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='currentteam',
            name='position',
            field=models.CharField(choices=[('select', 'Select'), ('Goalkeepers', 'Goalkeepers'), ('Forwards', 'Forwards'), ('Midfielders', 'Midfielders'), ('Defenders', 'Defenders')], default='All', max_length=20),
        ),
    ]
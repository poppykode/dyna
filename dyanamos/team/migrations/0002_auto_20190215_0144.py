# Generated by Django 2.1.5 on 2019-02-14 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentteam',
            name='position',
            field=models.CharField(choices=[('All', 'All'), ('Goalkeepers', 'Goalkeepers'), ('Forwards', 'Forwards'), ('Midfielders', 'Midfielders'), ('Defenders', 'Defenders')], default='All', max_length=20),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-20 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190220_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelwiththeteam',
            old_name='moment_of_the_match_image',
            new_name='best_team_image',
        ),
        migrations.AlterField(
            model_name='loyalty',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 20, 14, 0, 52, 507876)),
        ),
    ]

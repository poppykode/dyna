# Generated by Django 2.1.5 on 2019-02-18 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0007_auto_20190216_1610'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadGamePromo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_image', models.ImageField(blank=True, null=True, upload_to='match-game/')),
                ('date_played', models.DateField()),
                ('date_created', models.DateTimeField(null=True)),
                ('team_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixture_one', to='fixtures.Fixture')),
                ('team_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixture_two', to='fixtures.Fixture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]

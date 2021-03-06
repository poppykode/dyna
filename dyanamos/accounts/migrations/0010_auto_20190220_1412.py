# Generated by Django 2.1.5 on 2019-02-20 12:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190220_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='MomementOfTheMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_moment', models.CharField(blank=True, max_length=255)),
                ('image_of_the_moment', models.ImageField(blank=True, null=True, upload_to='fan/photo/')),
                ('date_created', models.DateTimeField(null=True)),
                ('published', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.AlterField(
            model_name='loyalty',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 20, 14, 12, 27, 49122)),
        ),
    ]

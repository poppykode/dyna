# Generated by Django 2.1.5 on 2019-02-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('All', 'All'), ('Goalkeepers', 'Goalkeepers'), ('Forwards', 'Forwards'), ('Midfielders', 'Midfielders'), ('Defenders', 'Defenders')], default='All', max_length=10)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('number', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='players/')),
                ('bio', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(blank=True, max_length=255)),
                ('height', models.CharField(blank=True, max_length=255)),
                ('weight', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]

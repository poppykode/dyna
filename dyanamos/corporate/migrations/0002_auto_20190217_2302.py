# Generated by Django 2.1.5 on 2019-02-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='name',
            new_name='button_text',
        ),
        migrations.AddField(
            model_name='slider',
            name='button_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_color',
            field=models.CharField(blank=True, default='#31387D', max_length=255),
        ),
        migrations.AddField(
            model_name='slider',
            name='heading',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='slider',
            name='heading_color',
            field=models.CharField(blank=True, default='#31387D', max_length=255),
        ),
    ]

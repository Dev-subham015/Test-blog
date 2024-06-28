# Generated by Django 5.0.6 on 2024-06-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-02 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_recipe_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='preparation',
        ),
        migrations.AddField(
            model_name='recipe',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=2700)),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='some ingredients'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_recipe_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='duration',
            field=models.CharField(default='0 hours, 0 minutes', max_length=50),
        ),
    ]

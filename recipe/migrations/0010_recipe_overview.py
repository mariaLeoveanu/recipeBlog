# Generated by Django 3.0.7 on 2020-07-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_auto_20200702_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='overview',
            field=models.TextField(default='No description.'),
        ),
    ]
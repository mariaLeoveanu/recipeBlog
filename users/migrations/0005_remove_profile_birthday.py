# Generated by Django 3.0.7 on 2020-07-04 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
    ]
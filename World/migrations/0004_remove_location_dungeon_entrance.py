# Generated by Django 3.0.2 on 2020-09-24 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('World', '0003_auto_20200921_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='dungeon_entrance',
        ),
    ]

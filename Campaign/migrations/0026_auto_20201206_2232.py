# Generated by Django 3.1.2 on 2020-12-06 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0025_auto_20201206_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quest',
            old_name='in_city',
            new_name='in_cities',
        ),
    ]

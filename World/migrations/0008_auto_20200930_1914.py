# Generated by Django 3.0.2 on 2020-09-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('World', '0007_auto_20200930_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='in_empire',
        ),
        migrations.AddField(
            model_name='empire',
            name='regions',
            field=models.ManyToManyField(blank=True, to='World.Region'),
        ),
    ]

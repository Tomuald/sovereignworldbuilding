# Generated by Django 3.0.2 on 2020-10-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_auto_20200928_1653'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_library',
            field=models.ManyToManyField(blank=True, to='Project.Project'),
        ),
    ]
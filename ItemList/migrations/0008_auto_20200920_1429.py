# Generated by Django 3.0.2 on 2020-09-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemList', '0007_auto_20200919_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=125),
        ),
    ]

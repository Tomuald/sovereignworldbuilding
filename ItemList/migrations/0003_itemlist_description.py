# Generated by Django 3.0.2 on 2020-09-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemList', '0002_auto_20200911_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
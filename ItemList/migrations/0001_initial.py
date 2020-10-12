# Generated by Django 3.0.2 on 2020-08-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('item_type', models.CharField(choices=[('W', 'Weapon'), ('A', 'Armor'), ('P', 'Potion'), ('S', 'Scroll'), ('C', 'Currency'), ('O', 'Other')], max_length=1)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

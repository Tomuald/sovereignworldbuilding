# Generated by Django 3.0.2 on 2020-10-07 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('World', '0011_auto_20201003_2340'),
        ('Campaign', '0011_auto_20201003_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='in_universe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World.Universe'),
        ),
    ]

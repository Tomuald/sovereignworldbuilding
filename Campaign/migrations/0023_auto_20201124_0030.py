# Generated by Django 3.1.2 on 2020-11-24 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('World', '0027_citydemographics_in_project'),
        ('Dungeon', '0010_roomloot_in_project'),
        ('Campaign', '0022_auto_20201124_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='in_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='World.area'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='in_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='World.city'),
        ),
        migrations.AlterField(
            model_name='questencounter',
            name='in_dungeon_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dungeon.room'),
        ),
        migrations.AlterField(
            model_name='questencounter',
            name='in_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='World.location'),
        ),
    ]
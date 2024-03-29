# Generated by Django 3.1.2 on 2020-11-24 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20201012_0103'),
        ('Dungeon', '0010_roomloot_in_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dungeon',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='room',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='roomloot',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='roomset',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
    ]

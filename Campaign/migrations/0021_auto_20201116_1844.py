# Generated by Django 3.1.2 on 2020-11-16 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20201012_0103'),
        ('Campaign', '0020_questencounterloot_in_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='in_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
    ]

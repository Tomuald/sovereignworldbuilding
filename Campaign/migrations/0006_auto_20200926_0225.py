# Generated by Django 3.0.2 on 2020-09-26 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
        ('Campaign', '0005_campaign_in_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='in_project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.Project'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-09 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20201012_0103'),
        ('World', '0016_auto_20201108_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='in_project',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
            preserve_default=False,
        ),
    ]
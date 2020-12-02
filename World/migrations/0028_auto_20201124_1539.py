# Generated by Django 3.1.2 on 2020-11-24 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20201012_0103'),
        ('World', '0027_citydemographics_in_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='city',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='cityquarter',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='empire',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='faction',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='location',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='locationloot',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='region',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='universe',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='worldencounter',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
        migrations.AlterField(
            model_name='worldencounterloot',
            name='in_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
    ]
# Generated by Django 3.1.2 on 2020-11-04 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('World', '0014_auto_20201103_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='landscape',
            field=models.URLField(blank=True, help_text='Provide a URL to an image file.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='landscape',
            field=models.URLField(blank=True, help_text='Provide a URL to an image file.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cityquarter',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empire',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='landscape',
            field=models.URLField(blank=True, help_text='Provide a URL to an image file..', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='npc',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='npc',
            name='portrait',
            field=models.URLField(blank=True, help_text='Provide a URL to an image file.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='landscape',
            field=models.URLField(blank=True, help_text='Provide a URL to an image file.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='worldencounter',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]

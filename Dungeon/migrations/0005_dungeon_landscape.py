# Generated by Django 3.1.2 on 2020-10-17 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dungeon', '0004_auto_20201012_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='dungeon',
            name='landscape',
            field=models.URLField(blank=True, help_text='Provide a URL to an image file. Preferably, to the actual file, and not a link to a search engine.', max_length=255, null=True),
        ),
    ]
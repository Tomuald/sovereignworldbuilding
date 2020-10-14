# Generated by Django 3.1.2 on 2020-10-12 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20201012_0103'),
        ('ItemList', '0009_itemlist_in_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='in_itemlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ItemList.itemlist'),
        ),
        migrations.AlterField(
            model_name='itemlist',
            name='in_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
    ]
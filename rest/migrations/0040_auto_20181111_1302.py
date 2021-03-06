# Generated by Django 2.0.6 on 2018-11-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0039_auto_20181104_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='road_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='road_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='road_name_abbr',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='road_operator_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

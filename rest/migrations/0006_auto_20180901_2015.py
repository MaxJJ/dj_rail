# Generated by Django 2.0.6 on 2018-09-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_cargo_shipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='cargo',
            name='unit_price',
            field=models.FloatField(null=True),
        ),
    ]

# Generated by Django 2.0.6 on 2018-09-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0010_auto_20180907_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='facturas',
        ),
        migrations.AddField(
            model_name='shipment',
            name='facturas',
            field=models.ManyToManyField(related_name='shipments_facturas', to='rest.Factura'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-11-04 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0036_railbill_shipment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='is_border',
            new_name='is_out',
        ),
    ]
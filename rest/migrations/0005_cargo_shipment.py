# Generated by Django 2.0.6 on 2018-09-01 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20180828_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='shipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='of_shipment', to='rest.Shipment'),
        ),
    ]
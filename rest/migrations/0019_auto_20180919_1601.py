# Generated by Django 2.0.6 on 2018-09-19 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0018_auto_20180919_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='rw_bill',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.Railbill'),
        ),
    ]
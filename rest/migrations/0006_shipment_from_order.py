# Generated by Django 2.0.4 on 2018-04-19 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20180420_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='from_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rest.Order'),
            preserve_default=False,
        ),
    ]
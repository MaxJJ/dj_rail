# Generated by Django 2.0.6 on 2018-09-17 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0013_auto_20180917_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='container',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='container', to='rest.Container'),
        ),
    ]

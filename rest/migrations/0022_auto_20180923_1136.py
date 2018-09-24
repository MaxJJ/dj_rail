# Generated by Django 2.0.6 on 2018-09-23 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0021_auto_20180921_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='cargo',
        ),
        migrations.AddField(
            model_name='factura',
            name='cargo',
            field=models.ManyToManyField(related_name='facturas_cargo', to='rest.Cargo'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='container',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='container', to='rest.Container'),
        ),
    ]

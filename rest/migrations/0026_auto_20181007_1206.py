# Generated by Django 2.0.6 on 2018-10-07 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0025_auto_20181007_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='container', to='rest.Container'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-10-26 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0030_auto_20181025_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.Unit'),
        ),
    ]

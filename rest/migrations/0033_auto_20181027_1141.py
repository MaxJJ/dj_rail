# Generated by Django 2.0.6 on 2018-10-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0032_auto_20181026_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='extra_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='factura',
            name='extra_total_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='factura',
            name='footer_first_str',
            field=models.TextField(blank=True, null=True),
        ),
    ]
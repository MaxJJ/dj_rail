# Generated by Django 2.0.6 on 2018-09-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0015_auto_20180917_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

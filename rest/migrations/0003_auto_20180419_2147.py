# Generated by Django 2.0.4 on 2018-04-19 18:47

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20180418_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'Shipment',
                'verbose_name_plural': 'Shipments',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='is_closed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='will_arrive',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 4, 19, 18, 47, 23, 685561, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='destination_place',
            field=models.ManyToManyField(blank=True, related_name='destination_place', to='rest.Place'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dispatch_place',
            field=models.ManyToManyField(blank=True, related_name='dispatch_place', to='rest.Place'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipments',
            field=models.ManyToManyField(blank=True, to='rest.Shipment'),
        ),
    ]
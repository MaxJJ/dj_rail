# Generated by Django 2.0.6 on 2018-06-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0018_auto_20180629_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='is_border',
            field=models.NullBooleanField(default=False),
        ),
    ]

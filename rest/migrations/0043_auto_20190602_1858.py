# Generated by Django 2.0.6 on 2019-06-02 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0042_place_kps_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kpsstation',
            old_name='Id',
            new_name='kps_id',
        ),
    ]

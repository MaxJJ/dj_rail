# Generated by Django 2.0.6 on 2019-06-02 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0041_auto_20190602_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='kps_fields',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kps_fields', to='rest.KpsStation'),
        ),
    ]

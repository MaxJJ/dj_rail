# Generated by Django 2.0.6 on 2018-10-26 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0031_auto_20181026_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.Package'),
        ),
    ]

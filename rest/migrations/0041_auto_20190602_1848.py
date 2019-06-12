# Generated by Django 2.0.6 on 2019-06-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0040_auto_20181111_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='KpsStation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('Id', models.IntegerField(blank=True, null=True)),
                ('Code', models.CharField(blank=True, max_length=100, null=True)),
                ('RouteId', models.IntegerField(blank=True, null=True)),
                ('StationDistrictId', models.IntegerField(blank=True, null=True)),
                ('StationDistrictName', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Open', models.CharField(blank=True, max_length=100, null=True)),
                ('ExpImpCode', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('CountryCode', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('CountryName', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('RailwayCodeD2', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('RailwayCode', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('RailwayName', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('AdministrationShortname', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('Paragraph', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('IsVnk', models.NullBooleanField()),
            ],
            options={
                'verbose_name': 'KpsStation',
                'verbose_name_plural': 'KpsStations',
            },
        ),
        migrations.AlterField(
            model_name='roadsection',
            name='road',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

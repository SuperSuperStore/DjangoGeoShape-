# Generated by Django 3.2.7 on 2021-10-04 22:47

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globe', '0004_district_subdistrict'),
    ]

    operations = [
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('loc', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326)),
            ],
        ),
    ]

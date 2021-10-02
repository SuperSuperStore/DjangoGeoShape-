# Generated by Django 3.2.5 on 2021-09-29 20:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thailand', '0004_auto_20210803_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('adm0_en', models.CharField(max_length=50)),
                ('adm0_th', models.CharField(max_length=50)),
                ('adm0_pcode', models.CharField(max_length=50)),
                ('adm0_ref', models.CharField(max_length=50)),
                ('adm0alt1en', models.CharField(max_length=50)),
                ('adm0alt2en', models.CharField(max_length=50)),
                ('adm0alt1th', models.CharField(max_length=50)),
                ('adm0alt2th', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('validon', models.DateField()),
                ('validto', models.DateField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]

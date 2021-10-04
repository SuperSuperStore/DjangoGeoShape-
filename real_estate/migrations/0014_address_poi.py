# Generated by Django 3.2.7 on 2021-10-04 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globe', '0006_alter_poi_loc'),
        ('real_estate', '0013_alter_address_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='poi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globe.poi'),
        ),
    ]

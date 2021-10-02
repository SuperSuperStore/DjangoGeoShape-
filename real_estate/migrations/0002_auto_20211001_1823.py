# Generated by Django 3.2.7 on 2021-10-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='id',
        ),
        migrations.RemoveField(
            model_name='property_listing',
            name='id',
        ),
        migrations.AlterField(
            model_name='address',
            name='building_number',
            field=models.CharField(default='something', max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property_listing',
            name='title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]

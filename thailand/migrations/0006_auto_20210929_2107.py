# Generated by Django 3.2.5 on 2021-09-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thailand', '0005_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='adm0_ref',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='adm0alt1en',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='adm0alt1th',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='adm0alt2en',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='adm0alt2th',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thailand', '0003_alter_thailandplaces_adm3_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thailandplaces',
            name='adm3alt1en',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='thailandplaces',
            name='adm3alt1th',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='thailandplaces',
            name='adm3alt2en',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='thailandplaces',
            name='adm3alt2th',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]

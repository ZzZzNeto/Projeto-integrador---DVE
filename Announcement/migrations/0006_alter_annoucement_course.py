# Generated by Django 4.1.1 on 2023-01-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Announcement', '0005_annoucement_creation_time_alter_annoucement_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annoucement',
            name='course',
            field=models.CharField(choices=[('ADS', 'Ads'), ('APICULTURA', 'Apicultura'), ('ALIMENTOS', 'Alimentos'), ('AGROINDUSTRIA', 'Agroindustria')], max_length=30, null=True),
        ),
    ]

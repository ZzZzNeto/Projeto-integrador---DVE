# Generated by Django 4.1.1 on 2022-12-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexternal',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]
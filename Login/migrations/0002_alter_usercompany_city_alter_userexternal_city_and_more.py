# Generated by Django 4.1.1 on 2023-01-10 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompany',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userexternal',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userexternal',
            name='schooling',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userinternal',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinternal',
            name='course',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinternal',
            name='period',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userinternal',
            name='schooling',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Period',
        ),
        migrations.DeleteModel(
            name='Schooling',
        ),
    ]
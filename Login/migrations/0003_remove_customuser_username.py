# Generated by Django 4.1.1 on 2022-12-31 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_delete_myuser_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]

# Generated by Django 4.1.1 on 2022-12-26 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50, verbose_name='course')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=20, verbose_name='Período')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=25, verbose_name='Tags de interesse')),
            ],
        ),
        migrations.CreateModel(
            name='Annoucement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_annoucement', models.ImageField(upload_to=None)),
                ('name_of_company', models.CharField(max_length=50, verbose_name='Nome da empresa')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('district', models.CharField(max_length=80, verbose_name='Bairro')),
                ('street', models.CharField(max_length=80, verbose_name='Rua')),
                ('number', models.CharField(max_length=10, verbose_name='N°')),
                ('registration_deadline', models.IntegerField(verbose_name='Prazo de inscrções')),
                ('requirements', models.CharField(max_length=255, verbose_name='Requisitos')),
                ('workload', models.CharField(max_length=2, verbose_name='CH semanal')),
                ('Vacancies', models.CharField(max_length=3, verbose_name='Vagas')),
                ('benefits', models.CharField(max_length=255, verbose_name='Benefícios')),
                ('activities', models.CharField(max_length=255, verbose_name='Atividades a serem desenvolvidas')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('linkedin', models.CharField(max_length=50, verbose_name='Linkedin')),
                ('whatsapp', models.CharField(max_length=50, verbose_name='Whatsapp')),
                ('instagram', models.CharField(max_length=50, verbose_name='Instagram')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefone')),
                ('curricular', models.BooleanField(default=False)),
                ('total_workload', models.CharField(max_length=5, verbose_name='CH total')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Announcement.course')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Announcement.period')),
                ('tags', models.ManyToManyField(to='Announcement.tags')),
            ],
        ),
    ]

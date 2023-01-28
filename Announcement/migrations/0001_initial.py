# Generated by Django 4.1.4 on 2023-01-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='', max_length=25, verbose_name='Tag')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='imgs/TagsPictures/', verbose_name='Image TAG')),
            ],
        ),
        migrations.CreateModel(
            name='Annoucement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_annoucement', models.ImageField(upload_to='imgs/StagesPictures/', verbose_name='Imagem do estagio')),
                ('name_of_company', models.CharField(max_length=50, verbose_name='Nome da empresa')),
                ('district', models.CharField(max_length=80, verbose_name='Bairro')),
                ('street', models.CharField(max_length=80, verbose_name='Rua')),
                ('number', models.CharField(max_length=10, verbose_name='N°')),
                ('registration_time', models.DateField(null=True, verbose_name='Prazo de inscricao')),
                ('requirements', models.CharField(default='Requisitos', max_length=500, verbose_name='Requisitos')),
                ('workload', models.CharField(max_length=2, verbose_name='CH semanal')),
                ('vacancies', models.CharField(max_length=3, verbose_name='Vagas')),
                ('period', models.CharField(choices=[('MATUTINO', 'Matutino'), ('VESPERTINO', 'Vespertino'), ('NOTURNO', 'Noturno')], max_length=10)),
                ('benefits', models.CharField(max_length=500, verbose_name='Benefícios')),
                ('activities', models.CharField(max_length=500, verbose_name='Atividades a serem desenvolvidas')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('linkedin', models.CharField(max_length=50, verbose_name='Linkedin')),
                ('whatsapp', models.CharField(max_length=50, verbose_name='Whatsapp')),
                ('instagram', models.CharField(max_length=50, verbose_name='Instagram')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefone')),
                ('curricular', models.BooleanField(default=False, null=True)),
                ('course', models.CharField(choices=[('ADS', 'Ads'), ('APICULTURA', 'Apicultura'), ('ALIMENTOS', 'Alimentos')], max_length=30)),
                ('total_workload', models.CharField(max_length=5, null=True, verbose_name='CH total')),
                ('tags', models.ManyToManyField(to='Announcement.tags')),
            ],
        ),
    ]

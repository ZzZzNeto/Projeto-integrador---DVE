from django.db import models
from django.conf import settings
from Login.models import CustomUser
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ValidationError

class Tags(models.Model):
    tag = models.CharField(max_length=25, verbose_name='Tag', default="")
    image = models.ImageField('Image TAG', upload_to='imgs/TagsPictures/', null=True, blank=True, default=None)

    def __str__(self):
        return self.tag

class Annoucement(models.Model):
    CHOICES_STATUS = (
    ("ATIVO", "Ativo"),
    ("FINALIZADO", "Finalizado"),
    ("PAUSADO", "Pausado"),
    )

    CHOICES_PERIOD = (
    ("MATUTINO", "Matutino"),
    ("VESPERTINO", "Vespertino"),
    ("NOTURNO", "Noturno"),
    )

    CHOICES_COURSE = (
    ("ADS", "Ads"),
    ("APICULTURA", "Apicultura"),
    ("ALIMENTOS", "Alimentos"),
    ("AGROINDUSTRIA", 'Agroindustria'),
    )

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="creator", editable=False)
    inscrits = models.ManyToManyField(CustomUser, blank=True)
    image_annoucement = models.ImageField('Imagem do estagio', upload_to='imgs/StagesPictures/')
    name_of_company = models.CharField(max_length=50, verbose_name='Nome da empresa')
    district = models.CharField(max_length=80, verbose_name='Bairro')
    street = models.CharField(max_length=80, verbose_name='Rua')
    number = models.CharField(max_length=10, verbose_name="N°")
    tags = models.ManyToManyField(Tags)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default="ATIVO")
    creation_time = models.DateField(verbose_name='Data de criação', default=timezone.now)
    registration_time = models.DateField(verbose_name='Prazo de inscricao', null=True)
    requirements = models.CharField(max_length=500, verbose_name="Requisitos", default="Requisitos")
    workload = models.CharField(max_length=2, verbose_name='CH semanal')
    vacancies = models.CharField(max_length=3, verbose_name='Vagas')
    period = models.CharField(max_length=10, choices=CHOICES_PERIOD)
    benefits = models.CharField(max_length=500, verbose_name='Benefícios')
    activities = models.CharField(max_length=500, verbose_name='Atividades a serem desenvolvidas')
    description = models.CharField(max_length=500, verbose_name='Descrição')
    email =  models.EmailField("E-mail")
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    whatsapp = models.CharField(max_length=50, verbose_name='Whatsapp')
    instagram = models.CharField(max_length=50, verbose_name='Instagram')
    phone = models.CharField(max_length=13, verbose_name='Telefone')
    curricular = models.BooleanField(default=False, null=True)
    course = models.CharField(max_length=30, choices=CHOICES_COURSE, null=True, default=False)
    total_workload = models.CharField(max_length=5, verbose_name="CH total", null=True)

    def __str__(self):
        return self.name_of_company

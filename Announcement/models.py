from django.db import models

class Tags(models.Model):
    tags = models.CharField(max_length=25, verbose_name='Tags de interesse')

    def __str__(self):
        return self.tags

class Period(models.Model):
    period = models.CharField(max_length=20, verbose_name='Período')

    def __str__(self):
        return self.period

class Course(models.Model):
    course = models.CharField(max_length=50, verbose_name='course')

    def __str__(self):
        return self.course

class Annoucement(models.Model):
    image_annoucement = models.ImageField('Imagem do estagio', upload_to='imgs/ProfilePictures/', null=True, blank=True, default=None)
    name_of_company = models.CharField(max_length=50, verbose_name='Nome da empresa')
    district = models.CharField(max_length=80, verbose_name='Bairro')
    street = models.CharField(max_length=80, verbose_name='Rua')
    number = models.CharField(max_length=10, verbose_name="N°")
    tags = models.ManyToManyField(Tags)
    registration_deadline = models.IntegerField(verbose_name='Prazo de inscrções')
    requirements = models.CharField(max_length=500, verbose_name="Requisitos")
    workload = models.CharField(max_length=2, verbose_name='CH semanal')
    vacancies = models.CharField(max_length=3, verbose_name='Vagas')
    period = models.ForeignKey(Period, on_delete= models.CASCADE)
    benefits = models.CharField(max_length=500, verbose_name='Benefícios')
    activities = models.CharField(max_length=500, verbose_name='Atividades a serem desenvolvidas')
    description = models.CharField(max_length=500, verbose_name='Descrição')
    email =  models.EmailField("E-mail")
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    whatsapp = models.CharField(max_length=50, verbose_name='Whatsapp')
    instagram = models.CharField(max_length=50, verbose_name='Instagram')
    phone = models.CharField(max_length=13, verbose_name='Telefone')
    curricular = models.BooleanField(default=False)
    course = models.OneToOneField(Course, on_delete= models.CASCADE)
    total_workload = models.CharField(max_length=5, verbose_name="CH total")

    

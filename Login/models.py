from django.db import models

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=50, verbose_name='city')

    def __str__(self):
        return self.city

class Course(models.Model):
    course = models.CharField(max_length=50, verbose_name='course')

    def __str__(self):
        return self.course

class Period(models.Model):
    period = models.CharField(max_length=25, verbose_name='period')

    def __str__(self):
        return self.period

class Schooling(models.Model):
    schooling = models.CharField(max_length=50, verbose_name='schooling')

    def __str__(self):
        return self.schooling

class Tags(models.Model):
    tags = models.CharField(max_length=25, verbose_name='Tags de interesse')

    def __str__(self):
        return self.tags

class ExternalUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.CharField(max_length=100, verbose_name='E-mail')
    password = models.CharField(max_length=20, verbose_name='Senha')
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    birth_date = models.DateField()
    city = models.OneToOneField(City, on_delete= models.CASCADE)
    schooling = models.OneToOneField(Schooling, on_delete= models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name

class InternalUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.CharField(max_length=100, verbose_name='E-mail')
    registration = models.CharField(max_length=30, verbose_name='Matricula')
    birth_date = models.DateField()
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    schooling = models.OneToOneField(Schooling, on_delete= models.CASCADE)
    city = models.OneToOneField(City, on_delete= models.CASCADE)
    period = models.OneToOneField(Period, on_delete= models.CASCADE)
    course = models.OneToOneField(Course, on_delete= models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name

class CompanyUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.CharField(max_length=100, verbose_name='E-mail')
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    whatsapp = models.CharField(max_length=50, verbose_name='Whatsapp')
    instagram = models.CharField(max_length=50, verbose_name='Instagram')
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ')
    phone = models.CharField(max_length=13, verbose_name='Telefone')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    district = models.CharField(max_length=80, verbose_name='Bairro')
    street = models.CharField(max_length=80, verbose_name='Rua')
    city = models.OneToOneField(City, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class CoordinationUser(models.Model):
    email = models.CharField(max_length=100, verbose_name='E-mail')
    instagram = models.CharField(max_length=50, verbose_name='Instagram')
    phone = models.CharField(max_length=13, verbose_name='Telefone')
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')

    def __str__(self):
        return "Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte | Campus Pau dos Ferros"
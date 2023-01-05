from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
from django.db.models import signals

# Create your models here.

class Schooling(models.Model):
    schooling = models.CharField(max_length=50, verbose_name='schooling')

    def __str__(self):
        return self.schooling

class City(models.Model):
    city = models.CharField(max_length=50, verbose_name='city', primary_key=True)

    def __str__(self):
        return self.city

class Tags(models.Model):
    tags = models.CharField(max_length=25, verbose_name='Tags de interesse')

    def __str__(self):

        return self.tags
class Course(models.Model):
    course = models.CharField(max_length=50, verbose_name='course')

    def __str__(self):
        return self.course

class Period(models.Model):
    period = models.CharField(max_length=25, verbose_name='period')

    def __str__(self):
        return self.period

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Informe um email...")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    is_external = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    email = models.EmailField("E-mail", unique=True)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    photo = models.ImageField('Imagem do perfil', upload_to='imgs/ProfilePictures/', null=True, blank=True, default=None)
    description = models.CharField(max_length=1000, default="Descrição")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = UserManager()

class UserCompany(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    whatsapp = models.CharField(max_length=50, verbose_name='Whatsapp')
    instagram = models.CharField(max_length=50, verbose_name='Instagram')
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ')
    phone = models.CharField(max_length=13, verbose_name='Telefone')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    district = models.CharField(max_length=80, verbose_name='Bairro')
    street = models.CharField(max_length=80, verbose_name='Rua')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.name

class UserExternal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    birth_date = models.DateField(null=True)
    city = models.ForeignKey(City, on_delete= models.CASCADE, null=True)
    schooling = models.ForeignKey(Schooling, on_delete= models.CASCADE, null=True)
    institution = models.CharField(max_length=50, verbose_name='Institution', default="Institution")
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.user.name

class UserInternal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    registration = models.CharField(max_length=50, verbose_name='Matricula')
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    birth_date = models.DateField(null=True)
    city = models.ForeignKey(City, on_delete= models.CASCADE, null=True)
    schooling = models.ForeignKey(Schooling, on_delete= models.CASCADE, null=True)
    tags = models.ForeignKey(Tags, on_delete= models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete= models.CASCADE, null=True)
    period = models.ForeignKey(Period, on_delete= models.CASCADE, null=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.user.name

"""class Course(models.Model):
    course = models.CharField(max_length=50, verbose_name='course')

    def __str__(self):
        return self.course

class Period(models.Model):
    period = models.CharField(max_length=25, verbose_name='period')

    def __str__(self):
        return self.period

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
        return "Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte | Campus Pau dos Ferros"""
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import BaseUserManager, AbstractUser
from auditlog.registry import auditlog
from DVE.models import BaseModel

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Informe um email...")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user.is_superuser:
            group = Group.objects.get(name="coordenacao")
            user.groups.add(group)
            user.name = "Coordenação"
            user.photo = "https://ead.ifrn.edu.br/ajuda/wp-content/uploads/2022/05/ifrn-logo.png"
            user.save()
            cordenacao = CoordinationUser.objects.create(user=user)
            cordenacao.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser, BaseModel):
    username = None
    name = models.CharField(max_length=50)
    email = models.EmailField("E-mail", unique=True)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    photo = models.ImageField('Imagem do perfil', upload_to='imgs/ProfilePictures/', null=True, blank=True, default=None)
    description = models.CharField(max_length=1000)

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
    city = models.CharField(max_length=100, null=True)
    Qcreated = models.IntegerField(default=0)

    def __str__(self):
        return self.user.name

class UserExternal(models.Model):

    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    favorites = models.ManyToManyField("Announcement.Annoucement", related_name="favoritosExternal")
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    birth_date = models.DateField(null=True)
    city = models.CharField(max_length=100, null=True)
    schooling = models.CharField(max_length=200, null=True, default="Não Informado")
    institution = models.CharField(max_length=50, verbose_name='Institution', default="Não Informado")
    tags = models.ManyToManyField("Announcement.Tags", related_name="tagsExternal")

    def __str__(self):
        return self.user.name

class UserInternal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    favorites = models.ManyToManyField("Announcement.Annoucement", related_name="favoritosInternal")
    registration = models.CharField(max_length=50, verbose_name='Matricula')
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    birth_date = models.DateField(null=True)
    city = models.CharField(max_length=100, null=True)
    period = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=100, null=True)
    tags = models.ManyToManyField("Announcement.Tags", related_name="tagsInternal")

    def __str__(self):
        return self.user.name

class CoordinationUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    instagram = models.CharField(max_length=50, verbose_name='Instagram')
    phone = models.CharField(max_length=13, verbose_name='Telefone')
    linkedin = models.CharField(max_length=50, verbose_name='Linkedin')
    Qcreated = models.IntegerField(default=0)

    def __str__(self):
        return "Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte | Campus Pau dos Ferros"

auditlog.register(CustomUser)
auditlog.register(UserCompany)
auditlog.register(UserExternal)
auditlog.register(UserInternal)
auditlog.register(CoordinationUser)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from django.db import transaction
from braces.forms import UserKwargModelFormMixin
from Announcement.models import Tags
from .models import UserExternal, UserCompany, UserInternal, CustomUser, CoordinationUser

class CustomUserInternalCreateForm(UserCreationForm):
    name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'name')

    @transaction.atomic
    def save(self, commit=True):
        group = Group.objects.get(name="EstudanteIFRN")
        user = super().save(commit=False)
        user.is_internal = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data["email"]
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])
        user.save()
        user.groups.add(group)
        internal = UserInternal.objects.create(user=user)
        internal.save()
        return user

class CustomUserExternalCreateForm(UserCreationForm):
    name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'name')

    @transaction.atomic
    def save(self, commit=True):
        group = Group.objects.get(name="Estudante")
        user = super().save(commit=False)
        user.is_external = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data["email"]
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])
        user.save()
        user.groups.add(group)
        external = UserExternal.objects.create(user=user)
        external.save()
        return user

class CustomUserCompanyCreateForm(UserCreationForm):
    name = forms.CharField(required=True)
    cnpj = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'name')

    @transaction.atomic
    def save(self, commit=True):
        group = Group.objects.get(name="Empresa")
        user = super().save(commit=False)
        user.is_company = True
        user.name = self.cleaned_data.get("name")
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.username = user.email
        user.save()
        user.groups.add(group)
        company = UserCompany.objects.create(user=user)
        company.cnpj = self.cleaned_data["cnpj"]
        company.save()
        return user

class CompanyChangeForm(UserKwargModelFormMixin, UserChangeForm):
    CHOICES_CITY = (
    ("Não informado", "Não informado"),
    ("Pau dos Ferros", "Pau dos Ferros"),
    ("Sousa", "Sousa"),
    ("Natal", "Natal"),
    )

    cnpj = forms.CharField(max_length=18) 
    linkedin = forms.CharField(max_length=50)
    whatsapp = forms.CharField(max_length=50)
    instagram = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=13)
    cep = forms.CharField(max_length=9)
    district = forms.CharField(max_length=80)
    street = forms.CharField(max_length=80)
    city = forms.ChoiceField(required=False,choices=CHOICES_CITY, initial="Sousa")

    class Meta:
        model = CustomUser
        fields = ['name','email','description', 'photo']

    def __init__(self, *args, **kwargs):
        super(CompanyChangeForm, self).__init__(*args, **kwargs)
        self.fields['city'].initial=self.user.usercompany.city

    def save(self, commit=True):
        user = super().save(commit)
        using = user.usercompany
        using.cnpj = self.cleaned_data['cnpj']
        using.linkedin = self.cleaned_data['linkedin']
        using.whatsapp = self.cleaned_data["whatsapp"]
        using.instagram = self.cleaned_data["instagram"]
        using.phone = self.cleaned_data["phone"]
        using.cep = self.cleaned_data["cep"]
        using.district = self.cleaned_data["district"]
        using.street = self.cleaned_data["street"]
        using.city = self.cleaned_data['city']
        using.save()
        return user

class ExternalChangeForm(UserKwargModelFormMixin, UserChangeForm):
    CHOICES_SCHOOLING = (
    ("Não informado", "Não informado"),
    ("Ensino medio completo", "Ensino medio completo"),
    ("Ensino superior completo", "Ensino superior completo"),
    ("Ensino fundamental completo", "Ensino fundamental completo"),
    )

    CHOICES_CITY = (
    ("Não informado", "Não informado"),
    ("Pau dos Ferros", "Pau dos Ferros"),
    ("Sousa", "Sousa"),
    ("Natal", "Natal"),
    )

    linkedin = forms.CharField(max_length=50)
    birth_date = forms.DateField()
    schooling = forms.ChoiceField(required=False,choices=CHOICES_SCHOOLING)
    institution = forms.CharField(max_length=50)
    city = forms.ChoiceField(required=False,choices=CHOICES_CITY)
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple, required = False)

    class Meta:
        model = CustomUser
        fields = ['name','email','description', 'photo']

    def __init__(self, *args, **kwargs):
        super(ExternalChangeForm, self).__init__(*args, **kwargs)
        self.fields['city'].initial=self.user.userexternal.city
        self.fields['schooling'].initial=self.user.userexternal.schooling

    def save(self, commit=True):
        user = super().save(commit)
        using = user.userexternal
        using.linkedin = self.cleaned_data['linkedin']
        using.birth_date = self.cleaned_data['birth_date']
        using.schooling = self.cleaned_data['schooling']
        using.institution = self.cleaned_data['institution']
        using.city = self.cleaned_data["city"]
        using.tags.set(self.cleaned_data["tags"])
        using.save()
        return user

class InternalChangeForm(UserKwargModelFormMixin, UserChangeForm):
    CHOICES_CITY = (
    ("Não informado", "Não informado"),
    ("Pau dos Ferros", "Pau dos Ferros"),
    ("Sousa", "Sousa"),
    ("Natal", "Natal"),
    )

    CHOICES_COURSE = (
    ("Não informado", "Não informado"),
    ("ADS", "ADS"),
    ("Alimentos", "Alimentos"),
    ("Apicultura", "Apicultura"),
    ("Quimica", "Quimica"),
    ("Informatica", "Informatica"),
    )

    CHOICES_PERIOD = (
    ("Não informado", "Não informado"),
    ("1º", "1º"),
    ("2º", "2º"),
    ("3º", "3º"),
    ("4º", "4º"),
    ("5º", "5º"),
    ("6º", "6º"),
    ("7º", "7º"),
    )

    linkedin = forms.CharField(max_length=50)
    birth_date = forms.DateField()
    city = forms.ChoiceField(required=False,choices=CHOICES_CITY)
    course = forms.ChoiceField(required=False, choices=CHOICES_COURSE)
    period = forms.ChoiceField(required=False, choices=CHOICES_PERIOD)
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple, required = False)

    class Meta:
        model = CustomUser
        fields = ['name','email','description', 'photo']

    def __init__(self, *args, **kwargs):
        super(InternalChangeForm, self).__init__(*args, **kwargs)
        self.fields['city'].initial=self.user.userinternal.city
        self.fields['course'].initial=self.user.userinternal.course
        self.fields['period'].initial=self.user.userinternal.period

    def save(self, commit=True):
        user = super().save(commit)
        using = user.userinternal
        using.linkedin = self.cleaned_data['linkedin']
        using.birth_date = self.cleaned_data['birth_date']
        using.city = self.cleaned_data["city"]
        using.course = self.cleaned_data["course"]
        using.period = self.cleaned_data["period"]
        using.tags.set(self.cleaned_data["tags"])
        using.save()
        return user

class CoordinationChangeForm(UserKwargModelFormMixin, UserChangeForm):
    linkedin = forms.CharField(max_length=50)
    instagram = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=13)

    class Meta:
        model = CustomUser
        fields = ['name','email','description', 'photo']

    def save(self, commit=True):
        user = super().save(commit)
        using = user.coordinationuser
        using.linkedin = self.cleaned_data['linkedin']
        using.instagram = self.cleaned_data["instagram"]
        using.phone = self.cleaned_data["phone"]
        using.save()
        return user
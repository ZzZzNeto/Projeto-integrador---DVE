from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from braces.forms import UserKwargModelFormMixin
from django import forms
from django.db import transaction

from .models import UserExternal, UserCompany, UserInternal, CustomUser, City, Schooling

class CustomUserInternalCreateForm(UserCreationForm):
    
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
        group = Group.objects.get(name="EmpresaCoordenacao")
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
    cnpj = forms.CharField(max_length=18)
    linkedin = forms.CharField(max_length=50)
    whatsapp = forms.CharField(max_length=50)
    instagram = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=13)
    cep = forms.CharField(max_length=9)
    district = forms.CharField(max_length=80)
    street = forms.CharField(max_length=80)
    city = forms.ModelChoiceField(required=False,queryset=City.objects.all())

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
        using.city = self.cleaned_data["city"]
        using.save()
        return user

class ExternalChangeForm(UserKwargModelFormMixin, UserChangeForm):
    linkedin = forms.CharField(max_length=50)
    birth_date = forms.DateField()
    schooling = forms.ModelChoiceField(required=False,queryset=Schooling.objects.all())
    institution = forms.CharField(max_length=50)
    city = forms.ModelChoiceField(required=False,queryset=City.objects.all())

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
        print(self.cleaned_data['birth_date'])
        using.birth_date = self.cleaned_data['birth_date']
        using.schooling = self.cleaned_data['schooling']
        using.institution = self.cleaned_data['institution']
        using.city = self.cleaned_data["city"]
        using.save()
        return user

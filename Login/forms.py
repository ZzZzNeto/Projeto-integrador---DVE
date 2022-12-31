from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import transaction

from .models import UserExternal, UserCompany, CustomUser

class CustomUserExternalCreateForm(UserCreationForm):
    name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'name')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_external = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data["email"]
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])
        user.save()
        external = UserExternal.objects.create(user=user)
        external.save()
        return user

"""class CustomUserExternalChangeForm(UserChangeForm):
    class Meta:
        model = UserExternal
        fields = ('name','linkedin','birth_date', 'city', 'schooling', 'tags')
"""
class CustomUserCompanyCreateForm(UserCreationForm):
    name = forms.CharField(required=True)
    cnpj = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'name')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        user.name = self.cleaned_data.get("name")
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.username = user.email
        user.save()
        company = UserCompany.objects.create(user=user)
        company.cnpj = self.cleaned_data["cnpj"]
        company.save()
        return user
"""
class CustomUserCompanyChangeForm(UserChangeForm):
    class Meta:
        model = UserCompany
        fields = ('name','linkedin','whatsapp', 'instagram', 'phone', 'cep', 'district', 'street', 'city')
"""
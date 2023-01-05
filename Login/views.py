from django.shortcuts import (HttpResponseRedirect, get_object_or_404, redirect, render)
from .models import UserExternal
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import UserFormKwargsMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,UpdateView, View)
from .models import UserCompany, UserExternal, CustomUser
from . import forms

class SignUpExternalView(CreateView):
    model = CustomUser
    form_class = forms.CustomUserExternalCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signIn.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response

class SignUpInternalView(CreateView):
    model = CustomUser
    form_class = forms.CustomUserExternalCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signIn.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response

class SignUpCompanyView(CreateView):
    model = CustomUser
    form_class = forms.CustomUserCompanyCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signInCompany.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response
        
class UserView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class UpdateUserCompanyView(LoginRequiredMixin, UserFormKwargsMixin, UpdateView):
    form_class = forms.CompanyChangeForm
    template_name = 'profileEdit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário editado com sucesso!")
        return response

class UpdateUserExternalView(LoginRequiredMixin, UserFormKwargsMixin ,UpdateView):
    form_class = forms.ExternalChangeForm
    model = CustomUser
    template_name = 'profileEdit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário editado com sucesso!")
        return response

class ForgotPasswordView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'forgotPassword.html')

class RedefinePasswordView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'redefinePassword.html')

class VerificationView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'verification.html')
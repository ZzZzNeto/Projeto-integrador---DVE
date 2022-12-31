from django.shortcuts import (HttpResponseRedirect, get_object_or_404, redirect, render)
from .models import UserExternal
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

class SignUpCompanyView(CreateView):
    model = CustomUser
    form_class = forms.CustomUserCompanyCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signInCompany.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

class CompanyUserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')
        
class CoordinationUserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class ExternalUserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class UserExternalView(View):
    template_name = 'profile.html'
    queryset = UserExternal.objects.all()
    model = UserExternal

    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class UserExternalUpdate(UpdateView):
    template_name = 'profile.html'
    model = UserExternal
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')
   
class UserExternalDelete(DeleteView):
    template_name = 'profile.html'
    queryset = UserExternal.objects.all()
    model = UserExternal
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')

class SignInCompanyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'signInCompany.html')

class ForgotPasswordView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'forgotPassword.html')

class RedefinePasswordView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'redefinePassword.html')

class VerificationView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'verification.html')

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/login.html')
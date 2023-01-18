from django.shortcuts import (HttpResponseRedirect, get_object_or_404, redirect, render)
from .models import UserExternal
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import UserFormKwargsMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,UpdateView, View)
from .models import UserCompany, UserExternal, CustomUser
from Announcement.models import Annoucement
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
    form_class = forms.CustomUserInternalCreateForm
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
        
class UserView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    queryset = Annoucement.objects.all()
    model = Annoucement

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
    template_name = 'profileEdit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário editado com sucesso!")
        return response

class UpdateUserInternalView(LoginRequiredMixin, UserFormKwargsMixin ,UpdateView):
    form_class = forms.InternalChangeForm
    template_name = 'profileEdit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário editado com sucesso!")
        return response

class UpdateCoordinationUserView(LoginRequiredMixin, UserFormKwargsMixin ,UpdateView):
    form_class = forms.CoordinationChangeForm
    template_name = 'profileEdit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário editado com sucesso!")
        return response

class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('login')

    login_url = 'login'
    template_name = 'deleteConfirmUser.html'

def Subscribe(request, pk):
    announcement = Annoucement.objects.get(id=pk)
    if request.user.groups.filter(name="Estudante") or request.user.groups.filter(name="EstudanteIFRN"):
        announcement.inscrits.add(request.user)
        messages.success(request, "Inscrição realizada!")
    else:
        messages.success(request, "Usuarios empresa não podem se inscrever em anuncios!")
    return HttpResponseRedirect(reverse('announcement', args=[str(pk)]))

def RemoveSubscribe(request, pk):
    announcement = Annoucement.objects.get(id=pk)
    announcement.inscrits.remove(request.user)
    messages.success(request, "Inscrição removida!")
    return HttpResponseRedirect(reverse('announcement', args=[str(pk)]))

def Favorite(request, pk):
    announcement = Annoucement.objects.get(id=pk)
    if request.user.groups.filter(name="EstudanteIFRN"):
        request.user.userinternal.favorites.add(announcement)
    else:
        request.user.userexternal.favorites.add(announcement)
    messages.success(request, "Adicionado aos favritos!")
    return HttpResponseRedirect(reverse('stages'))

def RemoveFavorite(request, pk):
    announcement = Annoucement.objects.get(id=pk)
    if request.user.groups.filter(name="EstudanteIFRN"):
        request.user.userinternal.favorites.remove(announcement)
    else:
        request.user.userexternal.favorites.remove(announcement)
    messages.success(request, "Removido dos favoritos")
    return HttpResponseRedirect(reverse('stages'))

def RemoveFavoriteProfile(request, pk):
    announcement = Annoucement.objects.get(id=pk)
    if request.user.groups.filter(name="EstudanteIFRN"):
        request.user.userinternal.favorites.remove(announcement)
    else:
        request.user.userexternal.favorites.remove(announcement)
    messages.success(request, "Removido dos favoritos")
    return HttpResponseRedirect(reverse('profile'))

class ForgotPasswordView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'forgotPassword.html')

class RedefinePasswordView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'redefinePassword.html')

class VerificationView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'verification.html')
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .models import CompanyUser, CoordinationUser, ExternalUser, InternalUser


class CompanyUserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')
        
class CoordinationUserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class ExternalUserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class InternalUserView(View):
    template_name = 'profile.html'
    queryset = InternalUser.objects.all()
    model = InternalUser

    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class InternalUserCreate(CreateView):
    template_name = 'singIn.html'
    model = InternalUser
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')

class InternalUserUpdate(UpdateView):
    template_name = 'profile.html'
    model = InternalUser
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')

class InternalUserDelete(DeleteView):
    template_name = 'profile.html'
    queryset = InternalUser.objects.all()
    model = InternalUser
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')






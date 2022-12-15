from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .models import User


class ExternalUser(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class InternalUser(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class UserCreate(CreateView):
    template_name = 'singIn.html'
    model = User
    fields = '__all__'
    success_url = reverse_lazy('Login:index')

class UserUpdate(UpdateView):
    template_name = 'profile.html'
    model = User
    fields = '__all__'
    success_url = reverse_lazy('Login:index')

class UserDelete(DeleteView):
    template_name = 'profile.html'
    queryset = User.objects.all()
    model = User
    fields = '__all__'
    success_url = reverse_lazy('Login:index')






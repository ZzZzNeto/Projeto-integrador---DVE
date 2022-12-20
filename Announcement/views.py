from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .models import Annoucement


class StagesView(ListView):
    template_name = 'stages.html'
    queryset = Annoucement.objects.all()

class AnnoucementView(DetailView):
    template_name = 'Annoucement.html'
    queryset = Annoucement.objects.all()
    model = Annoucement

class AnnoucementCreate(CreateView):
    template_name = 'Annoucement.html'
    model = Annoucement
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')

class AnnoucementUpdate(UpdateView):
    template_name = 'profile.html'
    model = Annoucement
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')

class AnnoucementDelete(DeleteView):
    template_name = 'profile.html'
    queryset = Annoucement.objects.all()
    model = Annoucement
    fields = '__all__'
    success_url = reverse_lazy('Login:profile')

class CandidatesView(ListView):
    template_name = 'seeCandidates.html'
    model = Annoucement
    queryset = Annoucement.objects.all()

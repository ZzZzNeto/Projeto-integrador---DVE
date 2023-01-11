from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .models import Annoucement, Tags
from .forms import AnnouncementForm

class StagesView(ListView):
    template_name = 'stages.html'
    queryset = Annoucement.objects.all()

class AnnoucementView(DetailView):
    template_name = 'announcementView.html'
    queryset = Annoucement.objects.all()
    model = Annoucement

class AnnoucementCreate(LoginRequiredMixin, CreateView):
    template_name = 'announcementCreateEdit.html'
    form_class = AnnouncementForm
    model = Annoucement
    success_url = reverse_lazy('profile')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Anúncio criados com sucesso!")
        return super(AnnoucementCreate, self).form_valid(form)

class AnnouncementUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'announcementCreateEdit.html'
    model = Annoucement
    form_class = AnnouncementForm
    success_url = reverse_lazy('profile')
    login_url = '/login'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Anúncio editado com sucesso!")
        return response
        
class AnnouncementDelete(LoginRequiredMixin, DeleteView):
    model = Annoucement
    queryset = Annoucement.objects.all()
    success_url = reverse_lazy('profile')

    login_url = 'login'
    template_name = 'deleteConfirm.html'

    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Anúncio excluído com sucesso!")
        return response

class CandidatesView(DetailView):
    template_name = 'seeCandidates.html'
    
    model = Annoucement
    queryset = Annoucement.objects.all()



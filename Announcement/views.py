from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .models import Annoucement, Tags


class StagesView(LoginRequiredMixin, ListView):
    template_name = 'stages.html'
    queryset = Annoucement.objects.all()
    login_url = '/user/login'

class AnnoucementView(LoginRequiredMixin, DetailView):
    template_name = 'Annoucement.html'
    queryset = Annoucement.objects.all()
    model = Annoucement

class AnnoucementCreate(LoginRequiredMixin, CreateView):
    template_name = 'announcementCreateEdit.html'
    model = Annoucement
    fields = 'image_annoucement', 'name_of_company', 'street', 'district', 'number','registration_deadline', 'tags', 'workload', 'vacancies', 'period', 'benefits', 'activities', 'email', 'phone','whatsapp', 'linkedin', 'instagram', 'description'
    success_url = reverse_lazy('profile')
    login_url = '/login'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(AnnoucementCreate, self).form_valid(form)

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

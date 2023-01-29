from django.shortcuts import (HttpResponseRedirect, get_object_or_404, redirect, render)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,UpdateView, View)
from .models import Annoucement, Tags
from .forms import AnnouncementForm, FilterForm

class StagesView(ListView):
    template_name = 'stages.html'
    model = Annoucement
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(StagesView, self).get_context_data(**kwargs)
        context['form'] = FilterForm()
        if self.request.GET: 
            context['search'] = self.request.GET.get("search")
            context['data'] = self.request.GET.getlist("tags")
            context['order'] = self.request.GET.get("order")
            context['period'] = self.request.GET.get("period")
        return context

    def get_queryset(self):
        if self.request.GET:
            kwargs = {}

            period = self.request.GET.get("period")
            if period:
                kwargs['period'] = period

            order = self.request.GET.get("order")
            if not order:
                order = "creation_time"
            
            search = self.request.GET.get("search")
            if search:
                kwargs['name_of_company__icontains'] = search

            tags = self.request.GET.getlist("tags")
            if tags:    
                queryset = Annoucement.objects.all()
                for tag in tags:
                    ids = list(queryset.filter(tags__id=tag).values_list("id", flat=True))
                    queryset = queryset.filter(id__in=ids)
                kwargs['id__in'] = ids

            if self.request.user.is_authenticated:
                for group in self.request.user.groups.all():
                    if group.name == "Estudante":
                        return Annoucement.objects.filter(curricular=False).filter(status = "ATIVO", **kwargs).order_by(order)
                    else:
                        return Annoucement.objects.all().filter(status = "ATIVO", **kwargs).order_by(order)
            else:
                return Annoucement.objects.all().filter(status = "ATIVO", **kwargs).order_by(order)
        else:
            if self.request.user.is_authenticated:
                for group in self.request.user.groups.all():
                    if group.name == "Estudante":
                        return Annoucement.objects.filter(curricular=False).filter(status = "ATIVO")
                    else:
                        return Annoucement.objects.all().order_by("-registration_time").filter(status = "ATIVO")
            else:
                return Annoucement.objects.all().filter(status = "ATIVO")

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
        for group in self.request.user.groups.all():
            if group.name == "coordenacao":
                self.request.user.coordinationuser.Qcreated += 1
                self.request.user.coordinationuser.save()
            else:
                self.request.user.usercompany.Qcreated += 1
                self.request.user.usercompany.save()
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
        form.instance.creator = self.request.user
        for group in self.request.user.groups.all():
            if group.name == "coordenacao":
                self.request.user.coordinationuser.Qcreated -= 1
                self.request.user.coordinationuser.save()
            else:
                self.request.user.usercompany.Qcreated -= 1
                self.request.user.usercompany.save()
        response = super().form_valid(form)
        messages.success(self.request, "Anúncio excluído com sucesso!")
        return response

class CandidatesView(DetailView):
    template_name = 'seeCandidates.html'
    
    model = Annoucement
    queryset = Annoucement.objects.all()



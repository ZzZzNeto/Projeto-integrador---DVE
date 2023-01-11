from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)
from Announcement.models import Annoucement


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    queryset = Annoucement.objects.all()

class FaqView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'faq.html')

class AboutUsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'aboutUs.html')
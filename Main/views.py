from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class FaqView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'faq.html')

class AboutUsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'aboutUs.html')
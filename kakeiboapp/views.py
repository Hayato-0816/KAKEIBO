from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

class BaseClass(TemplateView):
    template_name = 'base.html'
from django.shortcuts import render
from django.views import generic
from .models import *

class BaseClass(generic.TemplateView):
    template_name = 'base.html'
    model = MonthModel
    
    def get(self, request, pk):
        context = {}
        context['month_data'] = MonthModel.objects.get(pk=pk)
        return render(request, self.template_name, context)


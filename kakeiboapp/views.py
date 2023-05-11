from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import IncomeModel

class BaseClass(TemplateView):
    template_name = 'base.html'
    model = IncomeModel
    def get(self, request, pk):
        context = {}
        context['income_data'] = IncomeModel.objects.get(pk=pk)
        return render(request, self.template_name, context)
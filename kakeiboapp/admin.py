from django.contrib import admin
from .models import IncomeModel, TaxModel, ExpenseModel

# Register your models here.
admin.site.register(IncomeModel)
admin.site.register(TaxModel)
admin.site.register(ExpenseModel)
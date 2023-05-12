from django.db import models
from django.utils import timezone

# Create your models here.
# class MonthModels(models.Model):
#     month_date = models.DateField()
#     income = models.OneToOneField(IncomeModels, on_delete=models.CASCADE)
#     expense = models.   

class MonthModel(models.Model):
    date = models.DateField(blank=True, null=True)
    
    #給与
    income = models.IntegerField(
        verbose_name='総収入',
        blank=True,
        default=0,
        )
    salary = models.IntegerField(verbose_name='給料')
    commuting_allowance = models.IntegerField(verbose_name='交通費')

    #税金関連
    total_tax = models.IntegerField(
        verbose_name='税金/社会保険料',
        blank=True,
        default=0,
        )
    health_insurance = models.IntegerField(
        verbose_name='健康保険',
        blank=True,
        default=0,
        )
    welfare_pension = models.IntegerField(
        verbose_name='厚生年金',
        blank=True,
        default=0,
        )
    employment_insurance = models.IntegerField(
        verbose_name='雇用保険',
        blank=True,
        default=0,
        )
    income_tax = models.IntegerField(
        verbose_name='所得税',
        blank=True,
        default=0,
        )
    resident_tax = models.IntegerField(
        verbose_name='住民税',
        blank=True,
        default=0,
        )

#税率を計算して動かす仕組みにしたい
#税率は設定画面から変更が可能

    #支出関連
    total_expense = models.IntegerField(
        verbose_name='総支出',
        blank=True,
        default=0,
        )
    fixed_cost = models.IntegerField(
        verbose_name='固定費計',
        blank=True,
        default=0,
        )
    variable_cost = models.IntegerField(
        verbose_name='変動費計',
        blank=True,
        default=0,
        )

    #合計
    month_total = models.IntegerField(
        verbose_name='合計',
        blank=True,
        default=0,
        )
    
    def save(self, *args, **kwargs):
        self.income = (self.salary + self.commuting_allowance) - self.total_tax
        self.total_tax = self.health_insurance + self.welfare_pension + self.employment_insurance + self.income_tax + self.resident_tax
        self.total_expense = self.fixed_cost + self.variable_cost
        self.month_total = self.income - self.total_expense
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.date)
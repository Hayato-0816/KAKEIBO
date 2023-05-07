from django.db import models

# Create your models here.
# class MonthModels(models.Model):
#     month_date = models.DateField()
#     income = models.OneToOneField(IncomeModels, on_delete=models.CASCADE)
#     expense = models.   

class IncomeModel(models.Model):
    income = models.IntegerField(
        verbose_name='総収入',
        blank=True,
        default=0
        )
    income_date = models.DateField()
    salary = models.IntegerField(verbose_name='給料')
    commuting_allowance = models.IntegerField(verbose_name='交通費')
    total_tax = models.IntegerField(verbose_name='税金/社会保険料')

    def save(self, *args, **kwargs):
        self.income = (self.salary + self.commuting_allowance) - self.total_tax
        super().save(*args, **kwargs)

# TAX_CATEGORY = (('health_insurance','健康保険'),('welfare_pension','厚生年金'),('employment_insurance','雇用保険'),('income_tax','所得税'),('resident_tax','住民税'))
class TaxModel(models.Model):
    total_tax = models.IntegerField(
        verbose_name='税金/社会保険料',
        blank=True,
        default=0
        )
    tax_date = models.DateField()
    # category = models.CharField(
    #     max_length = 100,
    #     choices = TAX_CATEGORY
    # )
    health_insurance = models.IntegerField(
        verbose_name='健康保険',
        blank=True,
        default=0
        )
    welfare_pension = models.IntegerField(
        verbose_name='厚生年金',
        blank=True,
        default=0
        )
    employment_insurance = models.IntegerField(
        verbose_name='雇用保険',
        blank=True,
        default=0
        )
    income_tax = models.IntegerField(
        verbose_name='所得税',
        blank=True,
        default=0
        )
    resident_tax = models.IntegerField(
        verbose_name='住民税',
        blank=True,
        default=0
        )

    def save(self, *args, **kwargs):
        self.total_tax = self.health_insurance + self.welfare_pension + self.employment_insurance + self.income_tax + self.resident_tax
        super().save(*args, **kwargs)

#税率を計算して動かす仕組みにしたい
#税率は設定画面から変更が可能

class ExpenseModel(models.Model):
    total_expense = models.IntegerField(verbose_name='総支出')
    fixed_cost = models.IntegerField(verbose_name='固定費')
    variable_cost = models.IntegerField(verbose_name='変動費')

# class FixedCostModels(models.Model):


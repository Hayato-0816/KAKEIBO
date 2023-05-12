# Generated by Django 3.2 on 2023-05-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeiboapp', '0006_alter_incomemodel_income_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpenseModel',
        ),
        migrations.DeleteModel(
            name='TaxModel',
        ),
        migrations.RenameField(
            model_name='incomemodel',
            old_name='income_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='employment_insurance',
            field=models.IntegerField(blank=True, default=0, verbose_name='雇用保険'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='fixed_cost',
            field=models.IntegerField(default=1, verbose_name='固定費'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='health_insurance',
            field=models.IntegerField(blank=True, default=0, verbose_name='健康保険'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='income_tax',
            field=models.IntegerField(blank=True, default=0, verbose_name='所得税'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='resident_tax',
            field=models.IntegerField(blank=True, default=0, verbose_name='住民税'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='total_expense',
            field=models.IntegerField(default=1, verbose_name='総支出'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='variable_cost',
            field=models.IntegerField(default=1, verbose_name='変動費'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='welfare_pension',
            field=models.IntegerField(blank=True, default=0, verbose_name='厚生年金'),
        ),
        migrations.AlterField(
            model_name='incomemodel',
            name='total_tax',
            field=models.IntegerField(blank=True, default=0, verbose_name='税金/社会保険料'),
        ),
    ]

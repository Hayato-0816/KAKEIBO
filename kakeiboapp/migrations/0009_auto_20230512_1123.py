# Generated by Django 3.2 on 2023-05-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeiboapp', '0008_auto_20230512_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomemodel',
            name='month_total',
            field=models.IntegerField(blank=True, default=0, verbose_name='合計'),
        ),
        migrations.AlterField(
            model_name='incomemodel',
            name='fixed_cost',
            field=models.IntegerField(blank=True, default=0, verbose_name='固定費計'),
        ),
        migrations.AlterField(
            model_name='incomemodel',
            name='variable_cost',
            field=models.IntegerField(blank=True, default=0, verbose_name='変動費計'),
        ),
    ]

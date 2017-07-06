# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyDietTotals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('total_KCALS', models.IntegerField(default=0)),
                ('total_protein', models.IntegerField(default=0)),
                ('total_carbs', models.IntegerField(default=0)),
                ('total_fat', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='meal',
            name='KCALS',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='carbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='daily_diet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.DailyDietTotals'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='fat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='protein',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='DailyDiet',
        ),
    ]

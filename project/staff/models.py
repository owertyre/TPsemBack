from django import forms
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    companyName = models.CharField(max_length=100, verbose_name="Компания")
    positionName = models.CharField(max_length=100, verbose_name="Должность")
    hireDate = models.DateField(verbose_name="Дата приёма")
    fireDate = models.DateField(blank=True, null=True, verbose_name="Дата увольнения")
    salary = models.IntegerField(verbose_name="Ставка, руб.")
    fraction = models.IntegerField(verbose_name="Ставка, %")
    base = models.IntegerField(verbose_name="База, руб.")
    advance = models.IntegerField(verbose_name="Аванс, руб.")
    by_hours = models.BooleanField(default=True, verbose_name="Почасовая оплата")

    def __str__(self):
        return self.name
from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название филиала')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        ordering = ['name']

    def __str__(self):
        return self.name

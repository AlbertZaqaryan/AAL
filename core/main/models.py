from django.db import models

# Create your models here.

class HomeBG(models.Model):
    name1 = models.CharField('BG name1', max_length=30)
    name2 = models.CharField('BG name2', max_length=100)
    description = models.TextField('BG desc')
    img = models.ImageField('BG image', upload_to = 'media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeBG'
        verbose_name_plural = 'HomeBGS'


class Gaghapar(models.Model):
    name = models.CharField('Gaghapar name1', max_length=30)
    about = models.TextField('Gaghapar desc')
    img = models.ImageField('Gaghapar image', upload_to = 'media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gaghapar'
        verbose_name_plural = 'Gaghapars'

class Data1(models.Model):
    name = models.CharField('Place name', max_length=30)
    date = models.DateField('Date')
    nums = models.IntegerField('Numbers of travel')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Date1'
        verbose_name_plural = 'Dates1'
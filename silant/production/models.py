from django.db import models

from silant.service.models import Servis

class Model_tech(models.Model):
    nazvan = models.CharField(max_length = 255)
    opisanie = models.CharField(max_length = 255)

class Model_dvig(models.Model):
    nazvan = models.CharField(max_length = 255)
    opisanie = models.CharField(max_length = 255)

class Model_trasm(models.Model):
    nazvan = models.CharField(max_length = 255)
    opisanie = models.CharField(max_length = 255)

class Model_vmost(models.Model):
    nazvan = models.CharField(max_length = 255)
    opisanie = models.CharField(max_length = 255)

class Model_umost(models.Model):
    nazvan = models.CharField(max_length = 255)
    opisanie = models.CharField(max_length = 255)

class Mashina(models.Model):
    zavodsk_nomer = models.CharField(max_length = 255)
    model_tech = models.ForeignKey(Model_tech, on_delete=models.CASCADE)
    model_dvig = models.ForeignKey(Model_dvig, on_delete=models.CASCADE)
    nomer_dvig = models.CharField(max_length = 255)
    model_trasm = models.ForeignKey(Model_trasm, on_delete=models.CASCADE)
    nomer_transm = models.CharField(max_length = 255)
    model_vmost = models.ForeignKey(Model_vmost, on_delete=models.CASCADE)
    nomer_vmost = models.CharField(max_length = 255)
    model_umost = models.ForeignKey(Model_tech, on_delete=models.CASCADE)
    nomer_umost = models.CharField(max_length = 255)
    dogovor_postavki = models.CharField(max_length = 255)
    data_otgruzki = models.DateField(auto_now_add = True)
    polzovatel = models.CharField(max_length = 255)
    adres_polz = models.CharField(max_length = 255)
    komplekt = models.CharField(max_length = 255)
    klient = models.CharField(max_length = 255)
    servis_partn = models.ForeignKey(Servis, on_delete=models.CASCADE)


from django.db import models


class Servis(models.Model):
    nazvanie = models.CharField(max_length=255)
    opisanie = models.CharField(max_length=255)

class Vid_to(models.Model):
    nazvanie = models.CharField(max_length=255)
    opisanie = models.CharField(max_length=255)

class Otkaz(models.Model):
    nazvanie = models.CharField(max_length=255)
    opisanie = models.CharField(max_length=255)

class Vosstanovlenie(models.Model):
    nazvanie = models.CharField(max_length=255)
    opisanie = models.CharField(max_length=255)

class To(models.Model):
    id = models.ForeignKey('production.Mashina', to_field = 'zavodsk_nomer', primary_key=True, on_delete=models.CASCADE)
    vid_to = models.ForeignKey(Vid_to, on_delete=models.CASCADE)
    data_to = models.DateField(auto_now_add = True)
    narabotka = models.IntegerField()
    uzel_otkaza = models.ForeignKey(Otkaz, on_delete=models.CASCADE)
    # opisanie_otkaza =
    vosstanovlenie = models.ForeignKey(Vosstanovlenie, on_delete=models.CASCADE)
    chasti = models.CharField(max_length = 255)
    data_vosstanov = models.CharField(max_length = 255)
    vrem_prost = models.CharField(max_length = 255)
    servis = models.ForeignKey(Servis, on_delete=models.CASCADE)


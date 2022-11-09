from django.db import models

from silant.production.models import Mashina


class Servis (models.Model):
    nazvanie = models.CharField(max_length = 255)
    opisanie = models.CharField(max_length = 255)

class To(models.Model):
    id = models.ForeignKey(Mashina, to_field = zavodsk_nomer, on_delete=models.CASCADE)
    vid_to = models.CharField(max_length = 255)
    data_to = models.DateField(auto_now_add = True)
    narabotka = models.IntegerField()

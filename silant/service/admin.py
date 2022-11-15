from django.contrib import admin

from .models import Vid_to, Otkaz, Vosstanovlenie, Servis, To

# Register your models here.
admin.site.register(Vid_to)
admin.site.register(Otkaz)
admin.site.register(Vosstanovlenie)
admin.site.register(Servis)
admin.site.register(To)
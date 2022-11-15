from django.contrib import admin

from .models import Model_tech, Model_dvig, Model_trasm, Model_vmost, Model_umost, Mashina

# Register your models here.
admin.site.register(Model_tech)
admin.site.register(Model_dvig)
admin.site.register(Model_trasm)
admin.site.register(Model_vmost)
admin.site.register(Model_umost)
admin.site.register(Mashina)
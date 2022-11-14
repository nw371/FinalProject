from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from silant.production import views

router = routers.DefaultRouter()
router.register(r'Mashina', views.MashinaView, 'Mashina')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
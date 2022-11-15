from django.urls import path, include
from rest_framework import routers
from production import views

router = routers.DefaultRouter()
router.register(r'Mashina', views.MashinaViewSet, 'Mashina')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
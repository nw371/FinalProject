from django.urls import path, include
from rest_framework import routers
from service import views

router = routers.DefaultRouter()
router.register(r'Mashina', views.ServisViewSet, 'Servis')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('apis/', include(router.urls)),
]
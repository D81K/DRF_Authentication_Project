from django.urls import path, include
from .views import home, StudentMVS

from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', StudentMVS )

urlpatterns = [
    path('', include(router.urls))
]
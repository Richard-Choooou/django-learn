from django.urls import path, include
from rest_framework import routers

from core.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

from django.urls import path, include

from core import views
from core.api.router import router

urlpatterns = [
    path('register/', views.register, name='register')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.views_test, name='home')
]
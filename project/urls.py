from django.urls import path
from . import views

urlpatterns = [
  path('', views.Page1, name='Page1')
  ]
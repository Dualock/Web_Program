from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estadios', views.estadios, name='estadios'),
    path('estadio/<int:estadio_id>/', views.estadio, name='estadio'),
]

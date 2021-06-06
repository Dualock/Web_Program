from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('estadios/', views.estadios, name='estadios'),
    path('estadio/<int:estadio_id>/', views.estadio, name='estadio'),
    path('eventos/', views.eventos, name='eventos'),
]

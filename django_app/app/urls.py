from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('estadios/', views.estadios, name='estadios'),
    path('estadio/<int:estadio_id>/', views.estadio, name='estadio'),
    path('eventos/', views.eventos, name='eventos'),
    path('admin/', views.admin, name='admin'),
]

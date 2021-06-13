from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('estadio/<int:estadio_id>/', views.estadio, name='estadio'),
    path('estadio/delete/<int:estadio_id>/', views.delete_estadio, name='estadio'),
    path('estadios/', views.estadios, name='estadios'),
    path('estadios/<int:pagina>/', views.estadios, name="estadios"),
    path('eventos/', views.eventos, name='eventos'),
    path('admin/', views.admin, name='admin'),
    path('crearEstadio/', views.create_estadio, name='crear_estadio'),
    path('perfil/<str:user_username>/', views.perfil_view, name = 'perfil'),
    path('crearUsuarioAdmin/', views.create_admin, name = 'crear_user_admin'),
    path('tipoAsiento/create/', views.create_tipo_asiento, name = 'crear_tipo_asiento'),
]

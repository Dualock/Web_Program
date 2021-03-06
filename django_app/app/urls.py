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
    path('admin/', views.admin, name='admin'),
    path('crearEstadio/', views.create_estadio, name='crear_estadio'),
    path('perfil/<str:user_username>/', views.perfil_view, name = 'perfil'),
    path('crearUsuarioAdmin/', views.create_admin, name = 'crear_user_admin'),
    path('tipoAsiento/create/', views.create_tipo_asiento, name = 'crear_tipo_asiento'),
    path('partido/create/', views.create_partido, name = 'create_partido'),
    path('partido/delete/<int:partido_id>', views.delete_partido, name = 'delete_partido'),
    path('tipoAsiento/delete/<int:tipo_asiento_id>', views.delete_tipo_asiento, name = 'delete_tipo_asiento'),
    path('user/delete/<int:user_id>', views.delete_user, name = 'delete_user'),
    path('reserva/delete/<int:reserva_id>', views.delete_reserva, name = 'delete_reserva'),
    path('user/makestaff/<int:user_id>', views.make_staff_user, name = 'make_staff_user'),
    path('user/removestaff/<int:user_id>', views.remove_staff_user, name = 'remove_staff_user'),
    path('reserva/create/', views.create_reserva, name = 'create_reserva'),
]

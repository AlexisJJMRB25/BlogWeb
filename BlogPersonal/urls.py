"""BlogPersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Personal import views
from . import settings
from django.contrib.staticfiles.urls import static
from Personal.views import AgregarInformacionPersonal,ListadoInformacionPersonal,ActualizarInformacionPersonal, BorrarInformacionPersonal,ActualizarUsuario
from Personal.views import ListaContactanos, EliminarContactanos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contactos/', views.Contactos, name='Contactos'),
    path('SobreNosotrosWeb/', views.SobreNosotrosWeb, name='SobreNosotrosWeb'),
    path('CrearInformacionPersonal/', views.CrearInformacionPersonal, name='CrearInformacionPersonal'),
    path('ListadoInformacionPersonal/', ListadoInformacionPersonal.as_view(), name='ListadoInformacionPersonal'),
    path('AgregarInformacionPersonal/', AgregarInformacionPersonal.as_view(), name='AgregarInformacionPersonal'),
    path('ActualizarInformacionPersonal/<int:pk>/', ActualizarInformacionPersonal.as_view(), name='ActualizarInformacionPersonal'),
    path('BorrarInformacionPersonal/<int:pk>/', BorrarInformacionPersonal.as_view(), name='BorrarInformacionPersonal'),
    path('EditarInformacionPersonal/<int:id_InformacionPersonal>/', views.EditarInformacionPersonal, name='EditarInformacionPersonal'),
    path('EliminarInformacionPersonal/<int:id_InformacionPersonal>/', views.EliminarInformacionPersonal, name='EliminarInformacionPersonal'),
    path('listaSobreNosotros/', views.listaSobreNosotros, name='listaSobreNosotros'),
    path('crearSobreNosotros/', views.crearSobreNosotros, name='crearSobreNosotros'),
    path('editarSobreNosotros/<int:id_SobreNosotros>/', views.editarSobreNosotros, name='editarSobreNosotros'),
    path('eliminarSobreNosotros/<int:id_SobreNosotros>/', views.eliminarSobreNosotros, name='eliminarSobreNosotros'),
    path('admin_inicio/', views.admin_inicio, name='admin_inicio'),
    path('', views.Inicio, name='Inicio'),
    path('listaUsuarios/', views.listaUsuarios, name='listaUsuarios'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario'),
    path('ActualizarUsuario/<int:pk>/', ActualizarUsuario.as_view(), name='ActualizarUsuario'),
    path('eliminarUsuario/<int:id_usuario>/', views.eliminarUsuario, name='eliminarUsuario'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('Salir/', views.Salir, name='Salir'),
    path('ListaContactanos/', ListaContactanos.as_view(), name='ListaContactanos'),
    path('EliminarContactanos/<int:pk>/', EliminarContactanos.as_view(), name='EliminarContactanos'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

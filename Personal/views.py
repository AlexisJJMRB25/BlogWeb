from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from Personal.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def Contactos(request):
    informacion = InformacionPersonal.objects.all()
    if request.method == 'POST':
        form = Contactanos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Contactos')
    else:
        form = Contactanos()
    return render(request, 'contacto.html', {'form': form, 'informacion': informacion})


def SobreNosotrosWeb(request):
    lista = SobreNosotros.objects.all()
    return render(request, 'sobre_Nosotros.html', {'lista': lista})


def listaSobreNosotros(request):
    lista = SobreNosotros.objects.all()
    return render(request, 'listaSobreNosotros.html', {'lista': lista})


def crearSobreNosotros(request):
    if request.method == 'POST':
        form = SobreNosotrosDatos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listaSobreNosotros')
    else:
        form = SobreNosotrosDatos()
    return render(request, 'crearSobreNosotros.html', {'form': form})


def editarSobreNosotros(request, id_SobreNosotros):
    editar = get_object_or_404(SobreNosotros, pk=id_SobreNosotros)
    form = SobreNosotrosDatos(request.POST or None,
                              request.FILES or None, instance=editar)
    if form.is_valid():
        form.save()
        return redirect('listaSobreNosotros')
    return render(request, 'editarSobreNosotros.html', {'form': form, 'editar': editar})


def eliminarSobreNosotros(request, id_SobreNosotros):
    eliminar = get_object_or_404(SobreNosotros, pk=id_SobreNosotros)
    eliminar.delete()
    return redirect('listaSobreNosotros')


def admin_inicio(request):
    return render(request, 'admin_inicio.html')


def lista_informacionPersonal(request):
    return render(request, 'lista_informacionPersonal.html')


def CrearInformacionPersonal(request):
    if request.method == 'POST':
        form = InformacionPersonalDatos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_inicio')
    else:
        form = InformacionPersonalDatos()
    return render(request, 'crearInformacionPersonal.html', {'form': form})


class ListadoInformacionPersonal(ListView):
    model = InformacionPersonal
    template_name = 'admin_inicio.html'
    context_object_name = 'lista'
    queryset = InformacionPersonal.objects.all()


class AgregarInformacionPersonal(CreateView):
    model = InformacionPersonal
    template_name = 'crearInformacionPersonal.html'
    form_class = InformacionPersonalDatos
    sucess_url = reverse_lazy('ListadoInformacionPersonal')


class ActualizarInformacionPersonal(UpdateView):
    model = InformacionPersonal
    template_name='EditarInformacionPersonal.html'
    form_class=InformacionPersonalDatos
    success_url = reverse_lazy('ListadoInformacionPersonal')

class BorrarInformacionPersonal(DeleteView):
     model = InformacionPersonal
     template_name = 'informacionpersonal_confirm_delete.html'
     success_url = reverse_lazy('ListadoInformacionPersonal')



def EditarInformacionPersonal(request, id_InformacionPersonal):
    Personal = get_object_or_404(
        InformacionPersonal, pk=id_InformacionPersonal)
    form = InformacionPersonalDatos(request.POST or None, instance=Personal)
    if form.is_valid():
        form.save()
        return redirect('admin_inicio')
    return render(request, 'EditarInformacionPersonal.html', {'form': form, 'Personal': Personal})


def EliminarInformacionPersonal(request, id_InformacionPersonal):
    Personal = get_object_or_404(
        InformacionPersonal, pk=id_InformacionPersonal)
    Personal.delete()
    return redirect('admin_inicio')

def Inicio(request):
    return render(request, 'inicio.html')

def iniciarSesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Inicio')
        else:
            return redirect('iniciarSesion')
    else:
        return render(request, 'iniciar_sesion.html')
    
def Salir(request):
    logout(request)
    return redirect('Inicio')

def listaUsuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listaUsuarios.html', {'usuarios': usuarios})

def crearUsuario(request):
    if request.method == 'POST':
        form = UsuarioCaptura(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaUsuarios')
    else:
        form = UsuarioCaptura()
    return render(request, 'crearUsuarios.html', {'form': form})

class AgregarUsuario(CreateView):
    model = User
    template_name = 'crearUsuarios.html'
    form_class = UsuarioCaptura
    success_url = reverse_lazy('listaUsuarios')

class ActualizarUsuario(UpdateView):
    model = User
    form_class = UsuarioCaptura
    template_name = 'ActualizarUsuario.html'
    success_url = reverse_lazy('listaUsuarios')

def eliminarUsuario(request, id_usuario):
    eliminar = get_object_or_404(User, pk=id_usuario)
    eliminar.delete()
    return redirect('listaUsuarios')
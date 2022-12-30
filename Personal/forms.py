from django import forms
from Personal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Contactanos(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['Nombre', 'Correo', 'Telefono','Descripcion']
        widgets = {
            'Nombre': forms.TextInput(
                attrs = {'class':'form-control',
                'placeholder':'Nombre',
                'type':'text',
                }
            ),
            'Correo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Correo',
                    'type':'email',
                }
            ),
            'Telefono': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Telefono',
                    'type':'Phone',
                }
            ),
            'Descripcion':forms.Textarea(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Descripcion',
                }
            )
        }
class InformacionPersonalDatos(forms.ModelForm):
    class Meta:
        model = InformacionPersonal
        fields = ['Direccion','Telefono1','Telefono2','Correo1','Correo2']
        widgets = {
            'Direccion': forms.TextInput(
                attrs = {
                    'class':'form-control input-style',
                    'placeholder':'Direccion',
                    'type':'text',
                }
            ),
            'Telefono1': forms.TextInput(
                attrs = {
                    'class':'form-control input-style',
                    'placeholder':'Primer telefono',
                    'type':'text',
                }
            ),
            'Telefono2': forms.TextInput(
                attrs = {
                    'class':'form-control input-style',
                    'placeholder':'Segundo telefono',
                    'type':'text',
                }
            ),
            'Correo1': forms.TextInput(
                attrs = {
                    'class':'form-control input-style',
                    'placeholder':'Primer Correo',
                    'type':'email',
                }
            ),
            'Correo2': forms.TextInput(
                attrs = {
                    'class':'form-control input-style',
                    'placeholder':'Segundo Correo',
                    'type':'email',
                }
            ),
        }

class SobreNosotrosDatos(forms.ModelForm):
    class Meta:
        model = SobreNosotros
        fields = ['Imagen','Titulo','Descripcion']
        widgets = {
            'Titulo': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingresa un titulo',
                    'type':'text',
                }
            ),
            'Descripcion': forms.Textarea(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingresa la descripcion',
                }
            )
        }

class UsuariosDatos(forms.ModelForm):
    model = User
    fields = ['username', 'password']


class UsuarioCaptura(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username', 'password1','password2',]
        widgets = {
            'first_name': forms.TextInput(
                attrs = {'class':'form-control',
                'placeholder':'Nombres',
                'type':'text',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Apellidos',
                    'type':'text',
                }
            ),
            'email': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Correo',
                    'type':'email',
                }
            ),
            'username': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Usuario',
                    'type':'text',
                }
            ),
        }
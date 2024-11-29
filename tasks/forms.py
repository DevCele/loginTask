from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task, CustomUser


class TaskCreationForm(forms.ModelForm):
    """
    Formulario para la creación de tareas.
    """
    class Meta:
        model = Task
        fields = ['title', 'content', 'completed']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'title': 'Título',
            'content': 'Descripción',
            'completed': 'Completado',
        }


class CustomUserCreationForm(UserCreationForm):
    """
    Formulario para registrar nuevos usuarios.
    """
    class Meta:
        model = CustomUser
        fields = ['nombre_de_usuario', 'correo_electronico', 'edad', 'password1', 'password2']
        labels = {
            'nombre_de_usuario': 'Nombre de Usuario',
            'correo_electronico': 'Correo Electrónico',
            'edad': 'Edad',
            'password1': 'Contraseña',
            'password2': 'Confirmación de Contraseña',
        }


class CustomUserUpdateForm(forms.ModelForm):
    """
    Formulario para editar la información de un usuario.
    """
    class Meta:
        model = CustomUser
        fields = ['nombre_de_usuario', 'correo_electronico', 'edad']
        labels = {
            'nombre_de_usuario': 'Nombre de Usuario',
            'correo_electronico': 'Correo Electrónico',
            'edad': 'Edad',
        }


'''from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Task, CustomUser


class TaskCreationForm(forms.ModelForm):
    """
    Formulario para la creación de tareas.
    """
    class Meta:
        model = Task
        fields = ['title', 'content', 'completed']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'title': 'Título',
            'content': 'Descripción',
            'completed': 'Completado',
        }


class CustomUserCreationForm(UserCreationForm):
    """
    Formulario para registrar nuevos usuarios.
    """
    class Meta:
        model = CustomUser
        fields = ['nombre_de_usuario', 'correo_electronico', 'edad', 'password1', 'password2']
        labels = {
            'nombre_de_usuario': 'Nombre de Usuario',
            'correo_electronico': 'Correo Electrónico',
            'edad': 'Edad',
            'password1': 'Contraseña',
            'password2': 'Confirmación de Contraseña',
        }


class CustomUserUpdateForm(forms.ModelForm):
    """
    Formulario para editar la información de un usuario.
    """
    class Meta:
        model = CustomUser
        fields = ['nombre_de_usuario', 'correo_electronico', 'edad']
        labels = {
            'nombre_de_usuario': 'Nombre de Usuario',
            'correo_electronico': 'Correo Electrónico',
            'edad': 'Edad',
        }'''




"""from django import forms


class TaskCreationForm(forms.Form):
    title = forms.CharField(label='Título', max_length=255)  
    content = forms.CharField(label='Contenido', widget=forms.Textarea())"""  

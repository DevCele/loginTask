from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'correo_electronico', 
        'nombre_de_usuario', 
        'edad', 
        'es_personal', 
        'esta_activo', 
        'fecha_union'
    ]
    
    # Campos para filtrar en el admin
    list_filter = [
        'es_personal', 
        'esta_activo', 
        'fecha_union'
    ]
    
    # Campos para buscar
    search_fields = [
        'correo_electronico', 
        'nombre_de_usuario'
    ]
    
    # Configuración de fieldsets para el formulario de edición
    fieldsets = (
        (None, {
            'fields': (
                'correo_electronico', 
                'nombre_de_usuario', 
                'password'
            )
        }),
        ('Información Personal', {
            'fields': (
                'edad',
            )
        }),
        ('Permisos', {
            'fields': (
                'es_personal', 
                'esta_activo', 
                'is_superuser'
            )
        }),
        ('Fechas Importantes', {
            'fields': (
                'fecha_union', 
                'last_login'
            )
        }),
    )
    
    # Configuración de fieldsets para crear nuevos usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'correo_electronico', 
                'nombre_de_usuario', 
                'edad',
                'password1', 
                'password2',
                'es_personal', 
                'esta_activo'
            ),
        }),
    )
    
    # Ordenamiento por defecto
    ordering = ('correo_electronico',)

# Registrar modelos en el admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task)

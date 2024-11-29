from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('', lambda request: HttpResponseRedirect('/tasks/')),  # Redirige a `/tasks/`
     path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),  # Agrega ruta de login directa
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('tasks/', include('tasks.urls')),
#]

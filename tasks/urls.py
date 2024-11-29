from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.global_navigation, name='global_navigation'),
    path('tasks/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:task_id>/', views.detail, name='detail'),
    path('edit/<int:task_id>/', views.edit, name='edit'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('change-password/', views.change_password, name='change_password'),
    path('account/', views.account_details, name='account_details'),
    path('account/edit/', views.edit_account, name='edit_account'),
    path('account/delete/', views.delete_account, name='delete_account'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
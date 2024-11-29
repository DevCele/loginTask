from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from .models import Task
from .forms import TaskCreationForm, CustomUserCreationForm  # Changed from UserRegistrationForm to CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def global_navigation(request):
    return render(request, 'tasks/global_navigation.html')


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = []
    return render(request, 'tasks/index.html', {'tasks': tasks})


@login_required
def create(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskCreationForm()
    return render(request, 'tasks/create.html', {'form': form})


@login_required
def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/detail.html', {'task': task})


@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(instance=task)
    return render(request, 'tasks/edit.html', {'task': task, 'form': form})


@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/delete.html', {'task': task})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('tasks:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'tasks/change_password.html', {'form': form})


@login_required
def account_details(request):
    return render(request, 'tasks/account_details.html', {'user': request.user})


@login_required
def edit_account(request):
    if request.method == 'POST':
        user = request.user
        user.nombre_de_usuario = request.POST.get('username')
        user.correo_electronico = request.POST.get('email')
        user.edad = request.POST.get('age')
        user.save()
        return redirect('tasks:account_details')
    return render(request, 'tasks/edit_account.html', {'user': request.user})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/delete_account.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('tasks:global_navigation')


class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Changed from UserRegistrationForm
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:index')
    else:
        form = CustomUserCreationForm()  # Changed from UserRegistrationForm
    return render(request, 'tasks/register.html', {'form': form})



'''from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskCreationForm, UserRegistrationForm

def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = []
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def create(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskCreationForm()
    return render(request, 'tasks/create.html', {'form': form})

@login_required
def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.save()
        return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(initial={
            'title': task.title,
            'content': task.content,
        })
        return render(request, 'tasks/edit.html', {'task': task, 'form': form})

@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/delete.html', {'task': task})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('tasks:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'tasks/change_password.html', {'form': form})

@login_required
def account_details(request):
    return render(request, 'tasks/account_details.html', {'user': request.user})

@login_required
def edit_account(request):
    if request.method == 'POST':
        request.user.username = request.POST['username']
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('tasks:account_details')
    return render(request, 'tasks/edit_account.html', {'user': request.user})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/delete_account.html', {'user': request.user})

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})
'''





'''from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Task
from .forms import TaskCreationForm

def index(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtiene solo las tareas del usuario autenticado
        tasks = Task.objects.filter(user=request.user)
    else:
        # Si no está autenticado, no muestra tareas
        tasks = []
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def create(request):
    """
    Vista para crear una nueva tarea.
    """
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Asigna el usuario autenticado a la tarea
            task.save()
            return redirect('tasks:index')  # Redirige a la lista de tareas
    else:
        form = TaskCreationForm()

    return render(request, 'tasks/create.html', {'form': form})

@login_required
def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    params = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', params)

@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.save()
        return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(initial={
            'title': task.title,
            'content': task.content,
        })
        params = {
            'task': task,
            'form': form,
        }
        return render(request, 'tasks/edit.html', params)

@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    else:
        params = {
            'task': task,
        }
        return render(request, 'tasks/delete.html', params)

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'  '''
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login , authenticate
from .forms import CustomUserCreationForm , CustomUserChangeForm , UserProfileForm , TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tasks/register.html', {'form':form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    for task in tasks:
        task.mark_expired()
    return render(request, 'tasks/task_list.html', {'tasks':tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task':task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form':form})

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.deadline = request.POST.get('deadline', task.deadline)
        task.save()
        return redirect('task_detail', task_id=task.id)
    return render(request, 'tasks/task_form.html', {'task': task})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task':task})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'tasks/profile.html', {'form':form,'user':request.user})

@login_required
def view_own_profile(request):
    return render(request, 'tasks/view_profile.html', {'user': request.user})

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by('priority')
    return render(request, 'todo_app/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_app/task_detail.html', {'task': task})


def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'todo_app/task_edit.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/task_edit.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


def kanban_board(request):
    tasks_pending = Task.objects.filter(status='P')
    tasks_in_progress = Task.objects.filter(status='IP')
    tasks_completed = Task.objects.filter(status='C')
    tasks_on_hold = Task.objects.filter(status='OH')
    tasks_canceled = Task.objects.filter(status='X')

    context = {
        'tasks_pending': tasks_pending,
        'tasks_in_progress': tasks_in_progress,
        'tasks_completed': tasks_completed,
        'tasks_on_hold': tasks_on_hold,
        'tasks_canceled': tasks_canceled,
    }
    return render(request, 'todo_app/kanban_board.html', context)


@csrf_exempt
def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('status')

        status_map = {
            'pending': 'P',
            'in-progress': 'IP',
            'completed': 'C',
            'on-hold': 'OH',
            'canceled': 'X'
        }

        task = Task.objects.get(id=task_id)
        task.status = status_map.get(new_status, 'P')
        task.save()

        return JsonResponse({'status': 'success'})
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            todo = Todo.objects.create(text=text)
            return JsonResponse({
                'id': todo.id,
                'text': todo.text,
                'completed': todo.completed
            })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def toggle_todo(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({
            'id': todo.id,
            'completed': todo.completed
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_todo(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView  
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TasksList(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'




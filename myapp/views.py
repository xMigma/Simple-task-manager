from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def main(request):
    if request.method == 'POST':
        task = Task(title=request.POST['title'],
                    description=request.POST['description']).save()
    return render(request, 'main.html', {'tasks': Task.objects.all()})

def delete_task(request, id):
    if request.method == 'POST':
        Task.objects.get(id=id).delete()
    return redirect('/')
    

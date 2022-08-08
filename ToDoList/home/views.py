from django.shortcuts import render,redirect
from .models import NewTask

# Create your views here.


def saveInfo(request):
    if  request.method == 'POST':
        AddTask = request.POST['addtask']
        time= request.POST['time']
        add = NewTask(AddTask=AddTask,time=time)
        add.save()
    Add = NewTask.abstract.objects.all()
    return render(request,"index.html",{'Add':Add})


def index(request):
    Add = NewTask.abstract.objects.all()
    return render(request,"index.html",{'Add':Add})


def Delete(request,id):
    New = NewTask.abstract.objects.get(id=id)
    New.delete()
    return redirect('/')
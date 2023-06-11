from django.shortcuts import render, redirect
from app.models import Menu
from app.forms import MenuForm
from django.http import HttpRequest

def add(request):
    form=MenuForm
    return render(
        request,
        'app/home/addmenu.html',{
            'form':form
        }
    )
    

def store(request):
    if request.method=="POST":
        form=Menu()
        form.title=request.POST.get('title')
        form.description=request.POST.get('description')
        
        if len(request.FILES) != 0:
            form.image=request.FILES['image']
        form.save()
        return redirect('/menu')

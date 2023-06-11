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

def edit(request,id):
    assert isinstance(request, HttpRequest)
    if request.method=="GET":
        if id== 0:
            form=MenuForm
        else:
            menu=Menu.objects.get(pk=id)
            form=MenuForm(instance=menu)
        return render(
            request,
            'app/home/editmenu.html',{
                'form':form
            }
        )
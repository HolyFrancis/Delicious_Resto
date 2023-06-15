from django.shortcuts import render, redirect
from app.models import Menu
from app.forms import MenuForm
from django.http import HttpRequest
from django.contrib import messages

def index(request):

    menus= Menu.objects.all()
    return render(request, 'app/home/menus.html',{'menus':menus})

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
            menus=Menu.objects.get(pk=id)
            form=MenuForm(instance=menus)
        return render(
            request,
            'app/home/editmenu.html',{
                'form':form
            }
        )
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = MenuForm(request.POST)
        else:
            menu = Menu.objects.get(pk=id)
            form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu has been updated successfully !")
        return redirect('/menu')

def delete(request, id):
    menu=Menu.objects.get(pk=id)
    menu.delete()
    messages.success(request, "Menu has been removed successfully!")
    return redirect('/menu')
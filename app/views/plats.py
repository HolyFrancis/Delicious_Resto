from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpRequest
from app.models import Plat
from app.forms import PlatForm

def index(request):
    assert isinstance(request, HttpRequest)
    plats=Plat.objects.all()
    return render(request, 
                  'app/home/plats.html',
                  {'plats':plats})
def add(request):
    form=PlatForm
    return render(
        request,
        'app/home/addplat.html',{
            'form':form
        }
    )

def store(request):
    if request.method=="POST":
        form=PlatForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/plats')


def edit(request,id):
    assert isinstance(request, HttpRequest)
    if request.method=="GET":
        if id== 0:
            form=PlatForm
        else:
            plat=Plat.objects.get(pk=id)
            form=PlatForm(instance=plat)
        return render(
            request,
            'app/home/editplat.html',{
                'form':form
            }
        )
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = PlatForm(request.POST)
        else:
            Plat = Plat.objects.get(pk=id)
            form = PlatForm(request.POST, instance=Plat)
        if form.is_valid():
            form.save()
            messages.success(request, "Plat has been updated successfully !")
        return redirect('/plats')

def delete(request, id):
    Plat=Plat.objects.get(pk=id)
    Plat.delete()
    messages.success(request, "Plat has been removed successfully!")
    return redirect('/plats')
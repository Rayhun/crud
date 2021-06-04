from django.shortcuts import render, redirect
from .models import Info
from .forms import CreateInfo


def home(request):
    information = Info.objects.all()
    return render(request, 'home.html', {'info': information})


def create_info(request):
    if request.method == "POST":
        form = CreateInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateInfo()
        return render(request, 'create.html', {'form': form})


def update_info(request, pk):
    pk = Info.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateInfo(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateInfo(instance=pk)
        return render(request, 'create.html', {'form': form})

def delete_info(request, pk):
    info = Info.objects.get(pk=pk)
    info.delete()    
    return redirect("home")

from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import ToDo



def Home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title != "":
            ToDo.objects.create(title=title)
        return redirect('home')

    data = ToDo.objects.all()
    data_dict = {'data':data}
    return render(request,'home.html',context=data_dict)

def Delete(request,id=None):
    ToDo.objects.get(id=id).delete()
    return redirect('home')


def Complete(request,id=None):
    data = ToDo.objects.get(id=id)
    data.complete = True
    data.save()
    return redirect('home')

def InComplete(request, id=None):
    data = ToDo.objects.get(id=id)
    data.complete = False
    data.save()
    return redirect('home')
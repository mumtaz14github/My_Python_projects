from django.shortcuts import render, redirect
from .models import todomodel
from .forms import todos


def add(request):
    d1 = todomodel.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date')
        t1 = todomodel(name=name, priority=priority, date=date)
        t1.save()

    return render(request, 'index.html', {'detail': d1})


# def detail(request):
#     d1 = todomodel.objects.all()
#     return render(request, 'delete.html', {'detail': d1})


def delete(request, deid):
    if request.method == 'POST':
        del1 = todomodel.objects.get(id=deid)
        del1.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    up1 = todomodel.objects.get(id=id)
    f1 = todos(request.POST or None, instance=up1)
    if f1.is_valid():
        f1.save()
        return redirect('/')

    return render(request, 'update.html', {'f1': f1, 'up': up1})

# Create your views here.

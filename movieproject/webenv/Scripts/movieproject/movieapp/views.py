from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import movie


def index(request):
    m1 = movie.objects.all()
    context = {
        'movielist': m1
    }
    return render(request, 'index.html', context)


def detail(request, movieno):
    m2 = movie.objects.get(id=movieno)
    return render(request, 'detail.html', {'movieid': m2})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        user = movie(name=name, year=year, desc=desc, image=image)
        user.save()
        return redirect('/')

    return render(request, 'add.html')


# Create your views here.
def update(request, id):
    m1 = movie.objects.get(id=id)
    f1 = movieform(request.POST or None, request.FILES, instance=m1)
    if f1.is_valid():
        f1.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': f1, 'movie': m1})


def delete(request, id):
    if request.method == 'POST':
        d1 = movie.objects.get(id=id)
        d1.delete()
        return redirect('/')
    return render(request, 'delete.html')

from django.shortcuts import render

from .models import place
from .models import adv


def index(request):
    obj = place.objects.all()  # fetching objects from table place
    objs = adv.objects.all()
    context = {'imgkey': obj, 'advkey': objs}
    return render(request, 'index.html', context)

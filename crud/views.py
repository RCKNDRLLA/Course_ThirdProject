from django.shortcuts import render
from .models import Person
from django.http import HttpResponseRedirect, HttpResponseNotFound

def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})

def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
    return HttpResponseRedirect('/')

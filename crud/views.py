from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f'<h2>Привет, {name}, твой возраст: {age}</h2>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})


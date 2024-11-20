from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse

def index(request):
    userform = UserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            return HttpResponse(f'<h2>Hello, {name}</h2>')
        else:
            return render(request, 'index.html', {'form': userform})


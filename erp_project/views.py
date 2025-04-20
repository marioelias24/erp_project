from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def load_data(request):
    return HttpResponse("<p>Datos cargados exitosamente desde el servidor 🎉</p>")

def dashboard(request):
    return render(request, 'dashboard.html', {
        # en home no mostramos navbar
        'show_navbar': False,
    })

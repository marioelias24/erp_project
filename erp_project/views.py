from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def load_data(request):
    return HttpResponse("<p>Datos cargados exitosamente desde el servidor 🎉</p>")

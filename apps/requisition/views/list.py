# apps/requisition/views/list.py
from django.shortcuts import render
from ..models import Requisition

def requisition_list(request):
    """
    Muestra el listado de requisiciones.
    """
    requisitions = Requisition.objects.all()
    return render(request, 'requisition/list.html', {
        'requisitions': requisitions
    })

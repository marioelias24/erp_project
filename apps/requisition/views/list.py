from django.shortcuts import render
from apps.requisition.models import Requisition

def requisition_list(request):
    requisitions = Requisition.objects.all()
    return render(request, 'requisition/requisition_list.html', {'requisitions': requisitions})

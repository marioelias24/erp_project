from django.shortcuts import render, get_object_or_404
from apps.requisition.models import Requisition

def requisition_detail(request, pk):
    requisition = get_object_or_404(Requisition, pk=pk)
    return render(request, 'requisition/requisition_detail.html', {'requisition': requisition})

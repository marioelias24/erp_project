from django.shortcuts import get_object_or_404, render
from ..models import Requisition

def requisition_detail(request, pk):
    requisition = get_object_or_404(Requisition, pk=pk)
    return render(request, 'requisition/detail.html', {
        'requisition': requisition
    })

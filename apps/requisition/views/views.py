# apps/requisition/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Requisition
from .forms import RequisitionForm, RequisitionItemFormSet

def requisition_list(request):
    requisitions = Requisition.objects.all()
    return render(request, 'requisition/home.html', {
        'requisitions': requisitions,
        'show_navbar': True,
        'app_name': 'Solicitud de compra',
    })

def requisition_create(request):
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        formset = RequisitionItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            obj = form.save()
            formset.instance = obj
            formset.save()
            return redirect('requisition_list')
    else:
        form = RequisitionForm()
        formset = RequisitionItemFormSet()
    return render(request, 'requisition/create.html', {
        'form': form,
        'formset': formset,
        'show_navbar': True,
        'app_name': 'Solicitud de compra',
    })

def requisition_detail(request, pk):
    req = get_object_or_404(Requisition, pk=pk)
    return render(request, 'requisition/detail.html', {
        'requisition': req,
        'show_navbar': True,
        'app_name': 'Solicitud de compra',
    })

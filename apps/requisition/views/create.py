# apps/requisition/views/create.py
from django.shortcuts import render, redirect
from apps.requisition.forms import RequisitionForm, RequisitionItemFormSet

def requisition_create(request):
    form = RequisitionForm(request.POST or None)
    formset = RequisitionItemFormSet(request.POST or None, prefix='items')

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            requisition = form.save()
            formset.instance = requisition
            formset.save()
            return redirect('requisition_list')

    return render(request, 'requisition/create.html', {
        'form': form,
        'formset': formset,
    })

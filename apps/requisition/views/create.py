# apps/requisition/views/create.py
from django.shortcuts import render, redirect
from ..forms import RequisitionForm, RequisitionItemFormSet

def requisition_create(request):
    """
    Formulario para crear una nueva requisición junto a sus ítems.
    """
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        formset = RequisitionItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            requisition = form.save()
            formset.instance = requisition
            formset.save()
            return redirect('requisition_list')
    else:
        form = RequisitionForm()
        formset = RequisitionItemFormSet()

    return render(request, 'requisition/create.html', {
        'form': form,
        'formset': formset
    })

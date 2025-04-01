# apps/requisition/forms.py
from django import forms
from .models import Requisition, RequisitionItem
from django.forms import inlineformset_factory

class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = '__all__'
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date'}),
            'finalidad': forms.Textarea(attrs={
                'rows': 3,
                'cols': 40,
                'placeholder': 'Describa la razón de la compra...',
                'required': True,
                'class': 'campo-finalidad',
                'oninvalid': "this.setCustomValidity('Por favor, indique la finalidad de la compra')",
                'oninput': "setCustomValidity('')",
            }),
        }

RequisitionItemFormSet = inlineformset_factory(
    Requisition,
    RequisitionItem,
    fields=['articulo', 'cantidad'],
    extra=1,
    can_delete=True
)

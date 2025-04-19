# apps/requisition/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Requisition, RequisitionItem

class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['departamento', 'fecha_solicitud', 'cargo', 'responsable', 'finalidad']
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date'}),
            'finalidad': forms.Textarea(attrs={
                'rows': 3,
                'cols': 40,
                'placeholder': 'Describa la razón de la compra...',
                'required': True,
                'class': 'campo-finalidad',
                'oninvalid': "this.setCustomValidity('Por favor, indique la finalidad de la compra')",
                'oninput': "this.setCustomValidity('')",
            }),
        }

class RequisitionItemForm(forms.ModelForm):
    # articulo = forms.CharField(widget=forms.TextInput(attrs={
    #     'required': True,
    #     'placeholder': 'Nombre del artículo'
    # }))
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'required': True,
            'min': 1,
            'oninvalid': "this.setCustomValidity('La cantidad debe ser al menos 1')",
            'oninput': "this.setCustomValidity('')",
        })
    )

    class Meta:
        model = RequisitionItem
        fields = ['articulo', 'cantidad']
        widgets = {
            'articulo': forms.Textarea(attrs={
                'rows': 1,
                'style': 'width:100%; box-sizing:border-box; resize:vertical;',
                'placeholder': 'Nombre del artículo',
                'oninput': 'this.style.height="auto"; this.style.height=this.scrollHeight+"px";'
            }),
            'cantidad': forms.NumberInput(attrs={
                'required': True,
                'min': 1,
                'style': 'width:4em; box-sizing:border-box;',
                'oninvalid': "this.setCustomValidity('La cantidad debe ser al menos 1')",
                'oninput': "setCustomValidity('')",
            }),
            'finalidad': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Describa la razón de la compra...',
                'required': True,
                'class': 'campo-finalidad',
                # esto fuerza al 100% del ancho del contenedor
                'style': 'width:100%; box-sizing:border-box; min-height:6em;',
                'oninvalid': "this.setCustomValidity('Por favor, indique la finalidad de la compra')",
                'oninput': "this.setCustomValidity('')",
            }),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None:
            raise forms.ValidationError("Este campo es obligatorio")
        if cantidad < 1:
            raise forms.ValidationError("La cantidad debe ser al menos 1")
        return cantidad

RequisitionItemFormSet = inlineformset_factory(
    Requisition,
    RequisitionItem,
    form=RequisitionItemForm,   # <-- aquí enlazas tu nuevo form
    extra=1,
    can_delete=True
)

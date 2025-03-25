from django.urls import path
from .views import requisition_list  # Importamos la vista correctamente

urlpatterns = [
    path('', requisition_list, name='requisition_list'),  # Página de listado de requisiciones
]

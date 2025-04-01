from django.urls import path
from apps.requisition.views.list import requisition_list
from apps.requisition.views.create import requisition_create
from apps.requisition.views.detail import requisition_detail

urlpatterns = [
    path('', requisition_list, name='requisition_list'),
    path('crear/', requisition_create, name='requisition_create'),
    path('<int:pk>/', requisition_detail, name='requisition_detail'),
]

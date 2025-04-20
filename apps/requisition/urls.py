from django.urls import path
from .views.list import requisition_list
from .views.detail import requisition_detail
from .views.create import requisition_create

urlpatterns = [
    path('', requisition_list, name='requisition_list'),
    path('crear/', requisition_create, name='requisition_create'),
    path('<int:pk>/', requisition_detail, name='requisition_detail'),
]

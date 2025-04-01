from django.contrib import admin
from .models import Requisition, RequisitionItem

class RequisitionItemInline(admin.TabularInline):
    model = RequisitionItem
    extra = 1

@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    inlines = [RequisitionItemInline]

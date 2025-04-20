from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Requisition(models.Model):
    DEPARTAMENTO_CHOICES = [
        ('IT', 'Tecnología'),
        ('HR', 'Recursos Humanos'),
        ('FIN', 'Finanzas'),
        ('MKT', 'Marketing'),
        ('OPS', 'Operaciones'),
    ]

    CARGO_CHOICES = [
        ('analista', 'Analista'),
        ('jefe', 'Jefe de Departamento'),
        ('gerente', 'Gerente'),
        ('director', 'Director'),
    ]

    name = models.CharField(max_length=20, blank=True, null=True, unique=True)
    departamento = models.CharField(max_length=50, choices=DEPARTAMENTO_CHOICES)
    fecha_solicitud = models.DateField()
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    responsable = models.CharField(max_length=100)
    finalidad = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.responsable}"


class RequisitionItem(models.Model):
    requisition = models.ForeignKey(Requisition, related_name='items', on_delete=models.CASCADE)
    articulo = models.CharField(max_length=300)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.articulo} x {self.cantidad}"
    

def generar_codigo_secuencial():
    ultimo = Requisition.objects.order_by('-id').first()
    if not ultimo or not ultimo.name:
        return "SLD00001"

    try:
        ultimo_num = int(ultimo.name.replace("SLD", ""))
    except ValueError:
        ultimo_num = 0

    nuevo_num = ultimo_num + 1
    return "SLD{:05d}".format(nuevo_num)

@receiver(pre_save, sender=Requisition)
def asignar_codigo_requisition(sender, instance, **kwargs):
    if not instance.name:
        instance.name = generar_codigo_secuencial()

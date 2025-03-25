from django.db import models

class Requisition(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Nuevo campo agregado
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

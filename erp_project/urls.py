from django.contrib import admin
from django.urls import path, include  # 🔹 Asegúrate de incluir 'include'
from .views import home, load_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('load-data/', load_data, name='load_data'),  # Ruta para HTMX
    path('requisition/', include('apps.requisition.urls')),  # ✅ Asegurar que está bien referenciado
]

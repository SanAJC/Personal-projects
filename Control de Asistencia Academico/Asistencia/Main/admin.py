from django.contrib import admin
from .models import Asistencia

# Register your models here.

admin.site.register(Asistencia)

# Modificar el título en la parte superior del panel de administración
admin.site.site_header = "Control de Asistencia Academico"

# Modificar el título en la parte inferior del panel de administración
admin.site.site_title = "Panel Administrativo"

# Modificar el subtítulo en la página de inicio del panel de administración
admin.site.index_title = "Bienvenido al Panel de Administración"



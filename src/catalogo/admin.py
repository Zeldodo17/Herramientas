from django.contrib import admin

from .models import (
    Usuario,
    Herramientas,
    Clasificacion,
    Videos, 
    Unidades,
    Cursos
)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Herramientas)
admin.site.register(Clasificacion)

admin.site.register(Videos)
admin.site.register(Unidades)
admin.site.register(Cursos)
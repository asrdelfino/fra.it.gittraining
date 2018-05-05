from django.contrib import admin
from .models import AnagraficaUtente, Contratto, MandatoSepa

# Register your models here.

admin.site.register(AnagraficaUtente)
admin.site.register(Contratto)
admin.site.register(MandatoSepa)

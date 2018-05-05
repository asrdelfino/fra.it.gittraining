from .models import Contratto, AnagraficaUtente, MandatoSepa
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class ContrattoDetailCBV(DetailView):
    model = MandatoSepa
    template_name = "contratto.html"

class UtenteListCBV(ListView):
    model = AnagraficaUtente
    template_name = "lista_utenti.html"

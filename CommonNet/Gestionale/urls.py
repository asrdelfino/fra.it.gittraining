from django.urls import path

from .views import UtenteListCBV, ContrattoDetailCBV

urlpatterns = [
path('', UtenteListCBV.as_view(), name='lista_utenti'),
path('contratto/<int:pk>/', ContrattoDetailCBV.as_view(), name='contratto')
]

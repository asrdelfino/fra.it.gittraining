from django.db import models

# Create your models here.
class AnagraficaUtente(models.Model):
    nome = models.CharField("Nome", max_length=20)
    cognome = models.CharField("Cognome", max_length=20)
    indirizzo = models.CharField("Indirizzo",max_length=120, default = "Via", editable=True)
    civico = models.CharField("Civico",max_length=10)
    cap = models.CharField("Cap",max_length=5)
    citta = models.CharField("Città", max_length=20, default="Roma", editable=True)
    provincia = models.CharField("Provincia",max_length=2, default="RM", editable=True)
    codicefiscale = models.CharField ("Codice Fiscale", max_length=16)
    email = models.CharField("Email",max_length=30)
    telefono = models.CharField("Telefono", max_length=16)
    documento = models.CharField("Numero documento", max_length=20)
    enterilascio = models.CharField("Rilasciato da",max_length=20)
    datarilascio = models.DateField("Data rilascio")
    datascadenza = models.DateField("Data scadenza")

    def __str__(self):
        return self.cognome + " " + self.nome

    class Meta:
        verbose_name = "Utente"
        verbose_name_plural = "Utenti"

class Contratto(models.Model):
    contributoattivazione = models.FloatField("Contributo attivazione", default=200)
    canonemensile = models.FloatField("Canone mensile", default=20)
    indirizzoattivazione = models.CharField("Indirizzo attivazione", max_length=120, default="Via", editable=True)
    civicoattivazione = models.CharField("Civico",max_length=10)
    capattivazione = models.CharField("Cap", max_length=5)
    cittaattivazione = models.CharField("Città",max_length=20, default="Roma", editable=True)
    utente = models.ForeignKey(AnagraficaUtente, on_delete=models.CASCADE, related_name="utenti")
    provinciaattivazione = models.CharField("Provincia", max_length=2, default="RM", editable=True)
    datafirma = models.DateField("Data firma contratto")

    def __str__(self):
        return self.utente

        
    class Meta:
        verbose_name = "Contratto"
        verbose_name_plural = "Contratti"

class MandatoSepa(models.Model):
    riferimentomandato = models.CharField("Rif. mandato",max_length=20, default="D01L002", editable=True)
    nomedebitore = models.CharField("Nome debitore",max_length=20)
    cognomedebitore = models.CharField("Cognome debitore",max_length=20)
    codicefiscaledebitore = models.CharField ("Codice Fiscale", max_length=16)
    indirizzodebitore = models.CharField("Indirizzo",max_length=120, default="Via", editable=True)
    civicodebitore = models.CharField("Civico",max_length=10)
    capdebitore = models.CharField("Cap",max_length=5)
    comunedebitore = models.CharField("Comune", max_length=10, default="Roma", editable=True)
    codicefiscaledebitore = models.CharField("Codice Fiscale",max_length=16)
    provinciadebitore = models.CharField("Provincia",max_length=2, default="RM", editable=True)
    iban = models.CharField("Codice Iban", max_length=27)
    nomesottoscrittore = models.CharField("Nome sottoscrittore", blank=True, null=True, max_length=20)
    codicefiscalesottoscrittore = models.CharField ("Codice Fiscale", blank=True, null=True, max_length=16)
    cognomesottoscrittore = models.CharField("Cognome sottoscrittore", blank=True, null=True, max_length=20)
    ricorrente = models.BooleanField("Ricorrente",default=True)
    datafirmamandato = models.DateField("Data firma")
    contratto = models.ForeignKey(Contratto, on_delete=models.CASCADE, related_name="contratti")

    def __str__(self):
        return self.cognomedebitore + " " + self.nomedebitore

    class Meta:
        verbose_name = "Mandato Sepa"
        verbose_name_plural = "Mandati Sepa"

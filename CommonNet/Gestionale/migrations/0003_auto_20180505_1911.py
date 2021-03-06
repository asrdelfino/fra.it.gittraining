# Generated by Django 2.0.5 on 2018-05-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionale', '0002_auto_20180505_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagraficautente',
            name='cap',
            field=models.CharField(max_length=5, verbose_name='Cap'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='citta',
            field=models.CharField(default='Roma', max_length=20, verbose_name='Città'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='civico',
            field=models.CharField(max_length=10, verbose_name='Civico'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='codicefiscale',
            field=models.CharField(max_length=16, verbose_name='Codice Fiscale'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='cognome',
            field=models.CharField(max_length=20, verbose_name='Cognome'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='datarilascio',
            field=models.DateField(verbose_name='Data rilascio'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='datascadenza',
            field=models.DateField(verbose_name='Data scadenza'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='documento',
            field=models.CharField(max_length=20, verbose_name='Numero documento'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='email',
            field=models.CharField(max_length=30, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='enterilascio',
            field=models.CharField(max_length=20, verbose_name='Rilasciato da'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='indirizzo',
            field=models.CharField(default='Via', max_length=120, verbose_name='Indirizzo'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='nome',
            field=models.CharField(max_length=20, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='provincia',
            field=models.CharField(default='RM', max_length=2, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='anagraficautente',
            name='telefono',
            field=models.CharField(max_length=16, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='canonemensile',
            field=models.FloatField(default=20, verbose_name='Canone mensile'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='capattivazione',
            field=models.CharField(max_length=5, verbose_name='Cap'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='cittaattivazione',
            field=models.CharField(default='Roma', max_length=20, verbose_name='Città'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='civicoattivazione',
            field=models.CharField(max_length=10, verbose_name='Civico'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='contributoattivazione',
            field=models.FloatField(default=200, verbose_name='Contributo attivazione'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='datafirma',
            field=models.DateField(verbose_name='Data firma contratto'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='indirizzoattivazione',
            field=models.CharField(default='Via', max_length=120, verbose_name='Indirizzo attivazione'),
        ),
        migrations.AlterField(
            model_name='contratto',
            name='provinciaattivazione',
            field=models.CharField(default='RM', max_length=2, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='capdebitore',
            field=models.CharField(max_length=5, verbose_name='Cap'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='civicodebitore',
            field=models.CharField(max_length=10, verbose_name='Civico'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='codicefiscaledebitore',
            field=models.CharField(max_length=16, verbose_name='Codice Fiscale'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='cognomedebitore',
            field=models.CharField(max_length=20, verbose_name='Cognome debitore'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='cognomesottoscrittore',
            field=models.CharField(max_length=20, verbose_name='Cognome sottoscrittore'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='comunedebitore',
            field=models.CharField(default='Roma', max_length=10, verbose_name='Comune'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='datafirmamandato',
            field=models.DateField(verbose_name='Data firma'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='iban',
            field=models.CharField(max_length=27, verbose_name='Codice Iban'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='indirizzodebitore',
            field=models.CharField(default='Via', max_length=120, verbose_name='Indirizzo'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='nomedebitore',
            field=models.CharField(max_length=20, verbose_name='Nome debitore'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='nomesottoscrittore',
            field=models.CharField(max_length=20, verbose_name='Nome sottoscrittore'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='provinciadebitore',
            field=models.CharField(default='RM', max_length=2, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='ricorrente',
            field=models.BooleanField(default=True, verbose_name='Ricorrente'),
        ),
        migrations.AlterField(
            model_name='mandatosepa',
            name='riferimentomandato',
            field=models.CharField(default='D01L002', max_length=20, verbose_name='Rif. mandato'),
        ),
    ]

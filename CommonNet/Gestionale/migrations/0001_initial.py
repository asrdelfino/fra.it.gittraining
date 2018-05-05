# Generated by Django 2.0.5 on 2018-05-05 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnagraficaUtente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
                ('indirizzo', models.CharField(default='Via', max_length=120)),
                ('civico', models.CharField(max_length=10)),
                ('cap', models.CharField(max_length=5)),
                ('citta', models.CharField(default='Roma', max_length=20)),
                ('provincia', models.CharField(default='RM', max_length=2)),
                ('codicefiscale', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=16)),
                ('documento', models.CharField(max_length=20)),
                ('enterilascio', models.CharField(max_length=20)),
                ('datarilascio', models.DateField()),
                ('datascadenza', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contratto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributoattivazione', models.FloatField(default=200)),
                ('canonemensile', models.FloatField(default=20)),
                ('indirizzoattivazione', models.CharField(default='Via', max_length=120)),
                ('civicoattivazione', models.CharField(max_length=10)),
                ('capattivazione', models.CharField(max_length=5)),
                ('cittaattivazione', models.CharField(default='Roma', max_length=20)),
                ('provinciaattivazione', models.CharField(default='RM', max_length=2)),
                ('datafirma', models.DateField()),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utenti', to='Gestionale.AnagraficaUtente')),
            ],
        ),
        migrations.CreateModel(
            name='MandatoSepa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riferimentomandato', models.CharField(default='D01L002', max_length=20)),
                ('nomedebitore', models.CharField(max_length=20)),
                ('cognomedebitore', models.CharField(max_length=20)),
                ('indirizzodebitore', models.CharField(default='Via', max_length=120)),
                ('civicodebitore', models.CharField(max_length=10)),
                ('capdebitore', models.CharField(max_length=5)),
                ('comunedebitore', models.CharField(max_length=10)),
                ('provinciadebitore', models.CharField(default='RM', max_length=2)),
                ('codicefiscaledebitore', models.CharField(max_length=16)),
                ('iban', models.CharField(max_length=27)),
                ('nomesottoscrittore', models.CharField(max_length=20)),
                ('cognomesottoscrittore', models.CharField(max_length=20)),
                ('codicefiscalesottoscrittore', models.CharField(max_length=16)),
                ('ricorrente', models.BooleanField(default=True)),
                ('datafirmamandato', models.DateField()),
                ('contratto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratti', to='Gestionale.Contratto')),
            ],
        ),
    ]

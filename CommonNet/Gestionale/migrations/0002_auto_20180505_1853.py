# Generated by Django 2.0.5 on 2018-05-05 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionale', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anagraficautente',
            options={'verbose_name': 'Utente', 'verbose_name_plural': 'Utenti'},
        ),
        migrations.AlterModelOptions(
            name='contratto',
            options={'verbose_name': 'Contratto', 'verbose_name_plural': 'Contratti'},
        ),
        migrations.AlterModelOptions(
            name='mandatosepa',
            options={'verbose_name': 'Mandato Sepa', 'verbose_name_plural': 'Mandati Sepa'},
        ),
    ]

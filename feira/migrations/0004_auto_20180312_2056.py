# Generated by Django 2.0.2 on 2018-03-12 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feira', '0003_auto_20180312_2050'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArtigoCientifico',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='EventoCientifico',
        ),
        migrations.DeleteModel(
            name='PessoaFisica',
        ),
        migrations.DeleteModel(
            name='PessoaJuridica',
        ),
    ]

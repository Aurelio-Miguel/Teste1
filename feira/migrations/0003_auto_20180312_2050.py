# Generated by Django 2.0.2 on 2018-03-12 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feira', '0002_auto_20180312_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigocientifico',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='artigos',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='relizador',
        ),
    ]

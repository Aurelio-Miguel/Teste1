from django.db import models

# Create your models here.a

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=50)
    email = models.CharField('email', max_length=120)
    

class Evento(models.Model):
    nome = models.CharField('nome', max_length=150)
    eventoPrincipal = models.CharField('eventoPrincipal', max_length=200)
    dataEHoraDeInicio = models.DateTimeField(auto_now_add=True, blank=True)
    palavrasChave = models.CharField('palavrasChave', max_length=300)
    logotipo = models.CharField('logotipo', max_length=100)
    cidade = models.CharField('cidade', max_length=100)
    uf = models.CharField('uf', max_length=2)
    endereco = models.CharField('endereco', max_length=70)
    cep = models.CharField('cep', max_length=9)
    relizador = models.ForeignKey(Pessoa, related_name='eventos', null=False, blank=False, on_delete=models.CASCADE)


class EventoCientifico(models.Model):
    issn = models.CharField('issn', max_length=100)

class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=150)
    autores = models.CharField('autores', max_length=150)
    evento = models.ForeignKey(EventoCientifico, related_name='eventocientifico', null=True, blank=False, on_delete=models.CASCADE)


class Autor(models.Model):
    curriculo = models.CharField('curriculo', max_length=150) 
    #artigos = models.ForeignKey(ArtigoCientifico, related_name='artigos', null=True, blank=False, on_delete=models.CASCADE)

class PessoaJuridica(models.Model):
    cnpj = models.CharField('cnpj', max_length=50)
    razaoSocial = models.CharField('razaoSocial', max_length=550)

class PessoaFisica(models.Model):
    cpf = models.CharField('cnpj', max_length=50)







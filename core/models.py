from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='DATA DA CRIAÇÃO')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime("%d/%m/%Y %H:%M")

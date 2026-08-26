from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # util para gerar data e hora atual do projeto.

# Modelo que representa um Paciente.
# Atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem e ativo(true/false).
class Paciente(models.Model):
    nome = models.CharField(max_length=30) # nome do paciente limitado até 25 carácteres. 
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField() # email de contato do paciente.
    telefone = models.CharField( max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now) 
    mensagem = models.TextField(blank=True) # campo opcional, pode ficar em branco ou totalmente cheio, livre para mensagem.
    ativo = models.BooleanField(default=True) # campo de exclusão lógica
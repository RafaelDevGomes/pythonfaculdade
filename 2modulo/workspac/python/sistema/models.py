from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # util para gerar data e hora atual do projeto.

# Modelo que representa um Paciente.
# Atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem e ativo(true/false).
class Paciente(models.Model):
    nome = models.CharField(max_length=30) # nome do paciente limitado até 25 carácteres. 
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField() # email de contato do paciente.
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now) 
    mensagem = models.TextField(blank=True) # campo opcional, pode ficar em branco ou totalmente cheio, livre para mensagem.
    ativo = models.BooleanField(default=True) # campo de exclusão lógica
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Medico(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now)
    especialidade = models.CharField(max_length=20)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    crm = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Consulta(models.Model):
    consulta_nova = models.CharField(max_length=20, default='nova_consulta')
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_consulta = models.DateTimeField(default=timezone.now) #Data/hora da consulta
    ativa = models.BooleanField(default=True) # Campo de exclusão lógica
    observacao = models.TextField(blank=True) # Anotação opcional
    status = models.CharField(
        default='A',
        max_length=1,
        choices=[
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]
    )

    def __str__(self):
        return f'{self.consulta_nova}'
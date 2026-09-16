from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.TextField(blank=True)
    idade = models.IntegerField()
    cpf = models.TextField()
    endereco = models.TextField()
    telefone = models.TextField()
    ativo = models.BooleanField()
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.nome} {self.matricula}'

class Professor(models.Model):
    disciplina = models.TextField()
    nome = models.TextField()
    idade = models.IntegerField()
    endereco = models.TextField()
    telefone = models.IntegerField()
    ativo = models.BooleanField()
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.nome} {self.disciplina}'

class Turma(models.Model):
    turma = models.TextField()
    turno = models.CharField(max_length=10)
    professor_fk = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aluno_fk = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    ativo = models.BooleanField()
    data_cadastro = models.DateField(default=timezone.now)
    observacao = models.TextField()

    def __str__(self):
        return f'{self.turno} {self.turma}'
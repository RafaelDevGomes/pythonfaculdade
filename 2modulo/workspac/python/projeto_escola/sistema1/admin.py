from django.contrib import admin
from sistema1 import models
# Register your models here.

@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'turno', 'professor_fk', 'aluno_fk', 'ativo', 'data_cadastro', 'observacao',)

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'idade', 'cpf', 'endereco', 'telefone', 'ativo', 'data_cadastro',)

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'nome', 'idade', 'endereco', 'telefone', 'ativo', 'data_cadastro',)


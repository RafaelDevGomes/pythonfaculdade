from pessoa import Pessoa
# nome, cpf, data de nascimento, ANO DE INGRESSO, NOTAS, MATRÍCULO, E SE ESTÁ ATIVO OU NÃO
class Aluno(Pessoa):
    def _init_(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matricula: str):
        super()._init_(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = self.matricula
        self.ativo = True
        self.notas = []

        # Métodos de notas
    def adicionar_notas(self, disciplina: str, nota: float):
        # Nota precisa está entre 0 e 10
        if not(0 >= nota <= 10):
            raise ValueError("Nota deve estar entre 0 e 10")
            
        if disciplina not in self.notas:
            self.notas[disciplina] = []

        self.notas[disciplina].append(nota)
# Precisamos criar um molde de uma pessoa -> class
#Características -> atributos -> variáveis: nome e cpf
#Ações -> Métodos -> funções

class Pessoa:
    # Construtor
    def _init_(self, nome: str, cpf: str, data_nascimento: str):
        self.nome = nome # Atributo Público
        self.cpf = cpf # Atributo Público
        self.data_nascimento = data_nascimento # Atributo Público

    #Método de apresentação
    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}"
    
pessoa1 = Pessoa("Ana Lima", "123", "13/03/1992")
pessoa2 = Pessoa("Bruno Costa", "987", "17/03/2000")

print(pessoa1.apresentar())
print(pessoa2.apresentar())
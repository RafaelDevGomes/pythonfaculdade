# precisamos criar um molde de uma pessoa. => class
# caracteristicas -> atributos e são representadas via variáveis
# ações -> métodos são representadas via de funções

class Pessoa: 
    # constructor
    def __init__(self, nome, cpf, data_nasc: str):
        self.nome = nome
        self.cpf = cpf # cpf atributo publico 
        # self._cpf = cpf atributo privado 
        self.data_nasc = data_nasc
    # método de apresentação
    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}"
    
pessoa0 = Pessoa("Ana Lima", "123")
pessoa1 = Pessoa("Rafael Sigma", "123")

print(pessoa0.apresentar())
print(pessoa1.apresentar())





from paciente import Paciente
# classe filha, vai importar todas as informações de paciente

    # self.nome = nome
    #       self.data_nasc = data_nasc
    #       self.cpf = cpf
    #       self.telefone = telefone
    #       self.tipo_sang = tipo_sang
    #       self.numero_prontu = numero_prontu


class Pacienteparticular(Paciente):
    def __ini__(self, nome, data_nasc, cpf, telefone, tipo_sang, numero_prontu, forma_pagamento, desconto_fidelidade):
        super().__init__(nome, data_nasc, cpf, telefone, tipo_sang, numero_prontu)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade

    #sobre escrita de metodo = polimorfismo

    def calcular_valor_final(self, valor_consulta, taxa_urgencia):
        self.valor_consulta = valor_consulta
        self.taxa_urgencia = taxa_urgencia
        valor_consulta = valor_consulta * self.desconto_fidelidade
        return valor_consulta
        
        
    def exibir_informacoes(self):
      return f'''
      Nome: {self.nome}
      Data de Nascimento: {self.data_nasc}
      CPF: {self.cpf}
      Telefone: {self.telefone}
      Tipo Sanguíneo: {self.tipo_sang}
      Numero prontuário: {self.numero_prontu}
      '''

        
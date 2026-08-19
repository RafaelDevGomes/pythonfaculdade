# classe pai, ela que vai dominar tudo e vai ser uma classe abstrata - Superclass
    # nome
    # — string · nome completo do paciente

    # data_nascimento
    # — string · data de nascimento no formato "DD/MM/AAAA"

    # cpf
    # — string · CPF do paciente

    # telefone
    # — string · número de contato

    # tipo_sanguineo
    # — string · ex: "A+", "O-", "AB+"

    # numero_prontuario
    # — string · identificador único na clínica 

    ### Métodos (mínimo 2)
    # registrar_atendimento(tipo, custo)

    #     Exibe a informação de que o paciente passou por um atendimento do tipo informado, com custo de tanto.

    # exibir_informacoes(detalhado)

    #     Se False → exibe apenas nome, numero_prontuario e tipo_sanguineo
    #     Se True → exibe todos os 6 atributos

class Paciente:
   def __init__(self, nome, data_nasc, cpf, telefone, tipo_sang, numero_prontu ): #metodo constructor
      self.nome = nome
      self.data_nasc = data_nasc
      self.cpf = cpf
      self.telefone = telefone
      self.tipo_sang = tipo_sang
      self.numero_prontu = numero_prontu

   def exibir_informacoes(self):
      return f'''
      Nome: {self.nome}
      Data de Nascimento: {self.data_nasc}
      CPF: {self.cpf}
      Telefone: {self.telefone}
      Tipo Sanguíneo: {self.tipo_sang}
      Numero prontuário: {self.numero_prontu}
'''
   def registrar_atendimento(self, tipo, custo):
      self.tipo = tipo
      self.custo = custo

   
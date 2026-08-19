from paciente import Paciente
# classe filha, vai importar todas as informações de paciente

    # self.nome = nome
    #       self.data_nasc = data_nasc
    #       self.cpf = cpf
    #       self.telefone = telefone
    #       self.tipo_sang = tipo_sang
    #       self.numero_prontu = numero_prontu

class Pacienteconvenio(Paciente):
    def __init__(self, nome, data_nasc, cpf, telefone, tipo_sang, numero_prontu, nome_convenio, numero_carteirinha):
        super().__init__(nome, data_nasc, cpf, telefone, tipo_sang, numero_prontu)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha
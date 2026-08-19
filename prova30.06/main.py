from pacienteconvenio import Pacienteconvenio
from pacienteparticular import Pacienteparticular
from paciente import Paciente

#  Nome: {self.nome}
#       Data de Nascimento: {self.data_nasc}
#       CPF: {self.cpf}
#       Telefone: {self.telefone}
#       Tipo Sanguíneo: {self.tipo_sang}
#       Numero prontuário: {self.numero_prontu}
#       Numero da carteirinha: {self.numero_carteirinha}
#       Nome do convenio: {self.nome_convenio}
#       '''    
def main():

    pacientec1 = Pacienteconvenio("Rafael Gomes", "10/04/67", "123.456.789-02", "12 50219-2942", "Tipo -0", "prontuario 67", "convenio 67", "67")
    pacientep1 = Pacienteparticular("Rafael Gomes", "10/04/69", "123.456.789-02", "12 50219-2942", "Tipo -0", "prontuario 69")

    print('Detalhes do Paciente Convenio')
    print(pacientec1.exibir_informacoes())
    print('\n------------------------------')
    print('Detalhes do Paciente Particular')
    print(pacientep1.exibir_informacoes())
    print('\n------------------------------')
if __name__ == '__main__':
    main()

from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        if nome == " ": raise ValueError()
        self.__nome = nome 
        if cpf == " ": raise ValueError()
        self.__cpf = cpf
        if telefone == " ": raise ValueError()
        self.__telefone = telefone
        if nascimento > datetime.now() - timedelta(days = 365): raise ValueError()
        self.__nascimento = nascimento
    def idade(self):
        hoje = datetime.now()
        idade = hoje - self.__nascimento
        anos = idade.days // 365
        meses = (idade.days%365) // 30
        return f'{anos} Ano(s) e {meses} meses'
  

    def __str__(self):
        return f'Nome: {self.__nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\n Nascimento: {self.__nascimento}'
    
data1 = datetime.strftime("10/05/2003", "%d/%m/%Y")
print(data1)
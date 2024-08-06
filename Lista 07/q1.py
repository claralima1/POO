import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        if id == 0: raise ValueError()
        self.__id = id
        if nome == "": raise ValueError()
        self.__nome = nome
        if email == "": raise ValueError()
        self.__email = email
        if fone == 0: raise ValueError()
        self.__fone = fone

    def set_nome(self, n):
        if n == "": raise ValueError()
        self__.nome = n

    def set_email(self, e):
        if e == "": raise ValueError()
        self.__email = e

    def set_fone(self, f):
        if f == 0: raise ValueError()
        self.__fone = f
    
    def get_nome(self):
        return self.__nome
    
    def get_id(self):
        return self.__id
    
    def get_email(self):
        return self.__email
    
    def get_fone(self):
        return self.__fone

    def __str__(self):
        return f'{self.id} - {self.nome}'
    
def salvar_arquivo():  #método para salvar arquivo
    a = Cliente(1, "Douglas Crockford") #objeto cliente
    b = Cliente(2, "Jon Bosak") #Objetocliente
    clientes = [a,b]
    with open("clientes.json", mode ="w") as arquivo:
        json.dump(clientes, arquivo, default = vars)  

def abrir_arquivo():
    clientes = []
    with open("cientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
            c = Cliente(obj["id"], obj["nome"])
            clientes.append(c)
        
    for c in clientes:
        print(c)


abrir_arquivo()



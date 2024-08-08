import json
# Modelo - POJO POCO
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
class Venda:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id}"
    
class VendaItem:
    def __init__(self, id, qtd, preco):
        self.id = id
        self.qtd = qtd
        self.preco = preco

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"



# Persistência: Modelo -> Arquivo Json    
class Clientes:
    objetos = []
                    # atributo da classe e não de uma instância da classe
    @classmethod
    def inserir(cls, obj):      # create - C
        cls.abrir()             # abre a lista de clientes do arquivo
        id = 0                  # cálculo do id do novo objeto
        for x in cls.objetos:
            if x.id > id: id = x.id
        id += 1    
        obj.id = id             # novo objeto recebe o id calculado
        cls.objetos.append(obj) # insere o objeto a lista
        cls.salvar()            # salva o arquivo
    
    @classmethod
    def listar(cls):            # read - R
        cls.abrir()
        return cls.objetos  
    
    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.objetos:   # percorre a lista procurando o objeto com o id informado
            if x.id == id: return x
        return None      
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None:
            x.nome = obj.nome
            x.email = obj.email
            x.fone = obj.fone
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    @classmethod
    def salvar(cls):    
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("clientes.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)       

class VendasItens:
    vendas = []
    
    @classmethod
    def inserir(cls, item):
        cls.abrir()
        id = 0
        for x in cls.vendas:
            if x.id > id: id = x.id
        id +=1
        item.id = id
        cls.vendas.append(item)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.vendas

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.vendas:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar(cls, vend):
        x = cls.listar_id(vend.id)
        if x != None:
            x.qtd = vend.qtd
            x.preco = vend.preco
            cls.salvar()

    @classmethod
    def excluir(cls, vend):
        x = cls.listar_id(vend.id)
        if x != None:
            cls.vendas.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.vendas, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.vendas = []
        with open("vendar.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for vend in texto_arquivo:
                v = VendaItem(vend["id"], vend["qtd"], vend["preco"])
                cls.vendas.append(v)




class UI:
    @staticmethod
    def menu():
        print("Clientes")
        print("  1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()

    @staticmethod
    def cliente_inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        a = Cliente(0, nome, email, fone)
        Clientes.inserir(a)

    @staticmethod
    def cliente_listar():
        for cliente in Clientes.listar(): 
            print(cliente)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        a = Cliente(id, nome, email, fone)
        Clientes.atualizar(a)

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        a = Cliente(id, "", "", "")
        Clientes.excluir(a)

UI.main()
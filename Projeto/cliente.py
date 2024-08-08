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

class Produto:
    def __init__(self, id, d, p, e):
        self.id = id
        self.desc = d
        self.preco = p
        self.estoque = e

    def __str__(self):
        return f"{self.id} - {self.desc} - {self.preco} - {self.estoque}"

class Catgoria:
    def __init__(self, id, desc):
        self.id = id
        self.desc = desc
    def  __str__(self):
        return f"{self.id} - {self.desc}"

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
class Vendas:
    vendas = []

    @classmethod
    def inserir(cls, vends):
        cls.abrir()
        id = 0
        for x in cls.vendas:
            if x.id > id: id = x.id
        id += 1
        vends.id = id
        cls.vendas.append(vends)
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
    def atualizar(cls, v):
        x = cls.listar_id(v.id)
        if x!= None:
            x.id = v.id
            cls.salvar()

    @classmethod
    def excluir(cls, v):
        x = cls.listar_id(v.id)
        if x != None:
            cls.vendas.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.vendas, arquivo, defaut = vars)
    
    @classmethod
    def abrir(cls):
        cls.vendas = []
        with open("vendas.json", mode ="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for vend in texto_arquivo:
                v = Vendas(vend["id"])
                cls.vendas.append(v)

class VendasItens:
    vendas_itens = []
    
    @classmethod
    def inserir(cls, item):
        cls.abrir()
        id = 0
        for x in cls.vendas_itens:
            if x.id > id: id = x.id
        id +=1
        item.id = id
        cls.vendas_itens.append(item)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.vendas_itens

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.vendas_itens:
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
            cls.vendas_itens.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("vendas_itens.json", mode="w") as arquivo:
            json.dump(cls.vendas_itens, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.vendas_itens = []
        with open("vendar.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for vend in texto_arquivo:
                v = VendaItem(vend["id"], vend["qtd"], vend["preco"])
                cls.vendas_itens.append(v)

class Produtos:
    produtos = []

    @classmethod
    def inserir(cls, produto):
        cls.abrir()
        id = 0
        for x in cls.produtos:
            if x.id > id: id = x.id
        d +=1
        produto.id = id
        cls.produtos.append(produto)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        for x in cls.produtos:
            if x.id == id: return x
        return None
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.produtos:
            if x.id == id: return x
        return None

    @classmethod
    def atualizar(cls, prod):
        x = cls.listar_id(prod.id)
        if x != None:
            x.desc = prod.desc
            x.preco = prod.preco
            x.estoque = prod.estoque
            cls.salvar()
        
    @classmethod
    def excluir(cls, prod):
        x = cls.listar_id(prod.id)
        if x != None:
            cls.produtos.remove(prod)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.produtos, arquivo, default=vars)
    
    @classmethod
    def abrir(cls):
        cls.produtos = []
        with open("produtos.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for  prod in texto_arquivo:
                p = Produto(prod["id"], prod["descricção"], prod["preço"], prod["estoque"])
                cls.produtos.append(p)

class Categorias:
    categorias = []

    @classmethod
    def inserir(cls, c):
        cls.abrir()
        id = 0
        for x in cls.categorias:
            if x.id> id: id = x.id
        id += 1
        c.id = id
        cls.categorias.append(c)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.categorias

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.categorias:
            if x.id == id: return x
        return None

    @classmethod
    def atualizar(cls, c):
        x = cls.listar_id(c.id)
        if x != None:
            x.desc = c.desc
            cls.salvar()

    def excluir(cls, c):
        x= cls.listar_id(c.id)
        if x != None:
            cls.categorias.remove(c)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            texto_arquivo = json.load(arquivo)
            for c in texto_arquivo:
                c = Categorias(c["id"], c["descricão"])
                cls.categorias.append(c)
        

class UI:
    @staticmethod
    def menu():
        print("Clientes")
        print(" 1-Inserir Cliente, 1.1-Listar, 1.2-Atualizar, 1.3-Excluir, 9-Fim")
        print("Produtos")
        print(" 2 -Inserir Produto, 2.1-Listar Produto, 2.2-Atualizar Produto, 2.3-Excluir Produto, 9-Fim")
        print("Categorias")
        print(" 3 -Inserir categoria, 3.1-Listar categoria, 3.2-Atualizar categoria, 3.3-Excluir categoria, 9-Fim")
        
        return int(input("Escolha uma opção: "))
        
    
    
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            #CLIENTES
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            #PRODUTOS
            if op == 2: UI.inserir_produtos()
            if op == 2.1: UI.listar_produtos()
            if op == 2.2: UI.atualizar_produtos()
            if op == 2.3: UI.excluir_produto()
            #CATEGORIA  
            if op == 3: UI.inserir_categoria()
            if op == 3.1: UI.listar_categoria()
            if op == 3.2: UI.atualizar_categoria()
            if op == 3.3: UI.excluir_categoria()

    #CLIENTES
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

    #PRODUTOS       
    @staticmethod
    def inserir_produtos():
        desc = input("Informe qual o produto: ")
        valor = int(input("Informe o valor do produto: "))
        estoque = int(input("Informe a quantidade no estoque: "))
        p = Produto(0, desc, valor, estoque)
        Produtos.inserir(p)

    @staticmethod
    def listar_produtos():
        for produtos in Produtos.listar():
            print(produtos)

    @staticmethod
    def atualizar_produtos():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser atualizado: "))
        desc = input("Informe qual o novo produto: ")
        valor = int(input("Informe o valor do novo produto: "))
        estoque = int(input("Informe a quantidade atualizada do estoque: "))
        p = Produto(id, desc, valor, estoque)
        Produtos.atualizar(p)

    @staticmethod
    def excluir_produto():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser excluído: "))
        p = Produto(id, "","","")
        Produtos.atualizar(p)

    #CATEGORIA
    @staticmethod
    def inserir_categoria():
        categoria = input("Informe a categoria do produto: ")
        c = Catgoria(0, categoria)
        Categorias.inserir(c)

    @staticmethod
    def listar_categoria():
        for categoria in Categorias.listar():
            print(categoria)

    @staticmethod
    def atualizar_categoria():
        UI.listar_categoria()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        categoria = input("Informe a categoria do produto: ")
        c = Catgoria(id, categoria)
        Categorias.atualizar(c)
    
    @staticmethod
    def excluir_categoria():
        UI.listar_categoria()
        id = int(input("Informe a categoria a ser excluída: "))
        c = Catgoria(id, "")
        Categorias.excluir(c)


UI.main()
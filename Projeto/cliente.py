import json, datetime
# Modelo - POJO POCO
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    
    def set_nome(self, n):
        self.nome = n
    
    def get_nome(self):
        return self.nome

    def set_email(self, e):
        self.email = e
    
    def get_email(self):
        return self.email

    def set_fone(self, f):
        self.fone= f

    def get_fone(self):
        return self.fone

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Produto:
    def __init__(self, id, desc, preco, estoque):
        self.id = id
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
    
    def set_desc(self, d):
        self.desc = d
    
    def get_desc(self):
        return self.desc
    
    def set_preco(self, p):
        self.preco = p
    
    def get_preco(self):
        return self.preco
    
    def set_estoque(self, e):
        self.estoque = e
    
    def get_estoque(self):
        return self.estoque

    def __str__(self):
        return f"{self.id} - {self.desc} - {self.preco} - {self.estoque}"

class Categoria:
    def __init__(self, id, desc):
        self.id = id
        self.desc = desc

    def  __str__(self):
        return f"{self.id} - {self.desc}"
    
    def set_desc(self, d):
        self.desc = d
    
    def get_desc(self):
        return self.desc
    
class VendaItem:
    def __init__(self, id, qtd, p):
        self.id = id
        self.qtd = qtd
        self.preco = p
    
    def set_qtd(self, q):
        self.qtd = q
    
    def get_qtd(self):
        return self.qtd
    
    def set_preco(self, p):
        self.preco = p
    
    def get_preco(self):
        return self.preco
    
class Venda:
    def __init__(self, id):
        self.id = id
        #self.data = datetime.date()
        #self.carrinho = True
        #self.total


# Persistência: Modelo -> Arquivo Json    
class Clientes:
    objetos = []                # atributo da classe e não de uma instância da classe
    
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
class Produtos:
    produtos = []

    @classmethod
    def inserir(cls, produto):
        cls.abrir()
        id = 0
        for x in cls.produtos:
            if x.id > id: id = x.id
        id += 1
        produto.id = id
        cls.produtos.append(produto)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.produtos
    
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
            cls.produtos.remove(x)
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
                p = Produto(prod["id"], prod["desc"], prod["preco"], prod["estoque"])
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
        
    @classmethod
    def excluir(cls, c):
        x = cls.listar_id(c.id)
        if x != None:
            cls.categorias.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.categorias, arquivo, default=vars)
    
    @classmethod
    def abrir(cls):
        cls.categorias = []
        with open("categorias.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for c in texto_arquivo:
                cat = Categoria(c["id"], c["desc"])
                cls.categorias.append(cat)

class Vendas:
    vendas = []

    @classmethod
    def inserir(cls, v):
        cls.abrir()
        id = 0
        for x in cls.categorias:
            if x.id> id: id = x.id
        id += 1
        v.id = id
        cls.categorias.append(v)
        cls.salvar()

class UI:
    @staticmethod
    def menu():
        print("CLIENTES")
        print("  1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 20-Fim")
        print("\nPRODUTOS")
        print("  5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir, 20-Fim")
        print("\nCATEGORIAS")
        print("  9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir, 20-Fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 20:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            #PRODUTOS
            if op == 5: UI.inserir_produtos()
            if op == 6: UI.listar_produtos()
            if op == 7: UI.atualizar_produtos()
            if op == 8: UI.excluir_produto()
            #CATEGORIA
            if op == 9: UI.inserir_categoria()
            if op == 10: UI.listar_categoria()
            if op == 11: UI.atualizar_categoria()
            if op == 12: UI.excluir_categoria()
            

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
        valor = float(input("Informe o valor do produto: "))
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
        valor = float(input("Informe o valor do novo produto: "))
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
        c = Categoria(0, categoria)
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
        c = Categoria(id, categoria)
        Categorias.atualizar(c)
    
    @staticmethod
    def excluir_categoria():
        UI.listar_categoria()
        id = int(input("Informe o id da categoria a ser excluída: "))
        c = Categoria(id, "")
        Categorias.excluir(c)
    

UI.main()
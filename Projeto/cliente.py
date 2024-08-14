import json
import datetime
# Modelo - POJO POCO
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
    def set_nome(self, n):
        self.nome = n
    
    def set_email(self, e):
        self.email = e
    
    def set_nome(self, f):
        self.fone = f
    
    def get_nome(self):
        return self.nome
    
    def get_email(self):
        return self.email
    
    def get_fone(self):
        return self.fone 
    
    def set_id(self, id):
        self.id = id
    
    def get_idCliente(self):
        return self.id
    
class Venda:
    def __init__(self, id):
        self.id = id
        self.data = datetime.date
        if self.total != 0:
            self.carrinho = True
        else: self.carrinho = False
        self.total = VendaItem.qtd * VendaItem.preco
        self.idCliente = Cliente.id

    def set_idVenda(self, id):
        self.id = id
    
    def get_idVenda(self):
        return self.id
    
    def set_data(self, d):
        self.data = d
    
    def get_data(self):
        return self.data
    
    def get_carrinho(self):
        return self.carrinho
    
    def get_nome(self):
        return self.total

    def __str__(self):
        return f"{self.id}"
    
class VendaItem:
    def __init__(self, id, qtd, preco):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.idVenda = Venda.id
        self.idProduto = Produto.id
    
    def set_qtd(self, q):
        self.qtd = q
    
    def get_nome(self):
        return self.qtd

    def set_preco(self, p):
        self.preco = p
    
    def get_nome(self):
        return self.preco

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Produto:
    def __init__(self, id, d, p, e):
        self.id = id
        self.desc = d
        self.preco = p
        self.estoque = e
        self.idCategoria = Categoria.id

    def __str__(self):
        return f"{self.id} - {self.desc} - {self.preco} - {self.estoque}"

    def set_desc(self, d):
        self.desc = d
    
    def get_desc(self):
        return self.desc
    
    def set_preco(self, p):
        self.preco = p
    
    def get_nome(self):
        return self.preco

    def set_estoque(self, e):
        self.estoque = e
    
    def get_nome(self):
        return self.nome

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
        with open("vendas_itens.json", mode="r") as arquivo:
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
        

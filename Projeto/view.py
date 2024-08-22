from models.cliente import Cliente, Clientes, Produto, Produtos, Categoria, Categorias

class View:

    @staticmethod
    def cliente_inserir(nome, email, fone):
        a = Cliente(0, nome, email, fone)
        Clientes.inserir(a)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        a = Cliente(id, nome, email, fone)
        Clientes.atualizar(a)

    @staticmethod
    def cliente_excluir(id):
        a = Cliente(id, "", "", "")
        Clientes.excluir(a)

    #PRODUTOS       
    @staticmethod
    def inserir_produtos(desc, valor, estoque):
        p = Produto(0, desc, valor, estoque)
        Produtos.inserir(p)
    
    @staticmethod
    def listar_produtos():
        return Produtos.listar()

    @staticmethod
    def atualizar_produtos(id, desc, valor, estoque):
        p = Produto(id, desc, valor, estoque)
        Produtos.atualizar(p)

    @staticmethod
    def excluir_produto(id):
        p = Produto(id, "","","")
        Produtos.atualizar(p)
    
    #CATEGORIA
    @staticmethod
    def inserir_categoria(categoria):
        c = Categoria(0, categoria)
        Categorias.inserir(c)

    @staticmethod
    def listar_categoria():
        return Categorias.listar()

    @staticmethod
    def atualizar_categoria(id, categoria):
        c = Categoria(id, categoria)
        Categorias.atualizar(c)
    
    @staticmethod
    def excluir_categoria(id):
        c = Categoria(id, "")
        Categorias.excluir(c)

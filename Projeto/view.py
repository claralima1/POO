from cliente import Cliente, Clientes

class View:
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
        id = int(input("Informe a categoria a ser excluída: "))
        c = Categoria(id, "")
        Categorias.excluir(c)

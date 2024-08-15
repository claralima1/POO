from view import View
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
        View.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        for cliente in View.ciente_listar(): 
            print(cliente)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        View.cliente_atualizar(id, nome, email, fone)
        
    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)

    #PRODUTOS       
    @staticmethod
    def inserir_produtos():
        desc = input("Informe qual o produto: ")
        valor = int(input("Informe o valor do produto: "))
        estoque = int(input("Informe a quantidade no estoque: "))
        View.inserir_Produtos(desc, valor, estoque)
       
    @staticmethod
    def listar_produtos():
        for produtos in View.listar_produtos():
            print(produtos)

    @staticmethod
    def atualizar_produtos():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser atualizado: "))
        desc = input("Informe qual o novo produto: ")
        valor = int(input("Informe o valor do novo produto: "))
        estoque = int(input("Informe a quantidade atualizada do estoque: "))
        View.atualizar_produtos(id, desc, valor, estoque)

    @staticmethod
    def excluir_produto():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.excluir_produto(id)

    #CATEGORIA
    @staticmethod
    def inserir_categoria():
        categoria = input("Informe a categoria do produto: ")
        View.inserir_categoria(0, categoria)

    @staticmethod
    def listar_categoria():
        for categoria in View.listar_categoria:
            print(categoria)

    @staticmethod
    def atualizar_categoria():
        UI.listar_categoria()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        categoria = input("Informe a categoria do produto: ")
        View.atualizar_categoria(id, categoria)
    
    @staticmethod
    def excluir_categoria():
        UI.listar_categoria()
        id = int(input("Informe a categoria a ser excluída: "))
        View.excluir_categoria(id)



UI.main()
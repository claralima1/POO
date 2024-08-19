from view import View

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
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        View.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        for cliente in View.cliente_listar(): 
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
        valor = float(input("Informe o valor do produto: "))
        estoque = int(input("Informe a quantidade no estoque: "))
        View.inserir_produtos(desc, valor, estoque)
    
    @staticmethod
    def listar_produtos():
        for produtos in View.listar_produtos():
            print(produtos)

    @staticmethod
    def atualizar_produtos():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser atualizado: "))
        desc = input("Informe qual o novo produto: ")
        valor = float(input("Informe o valor do novo produto: "))
        estoque = int(input("Informe a quantidade atualizada do estoque: "))
        View.atualizar_produtos(id, desc, valor,estoque)

    @staticmethod
    def excluir_produto():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.cliente_excluir(id)

     #CATEGORIA
    @staticmethod
    def inserir_categoria():
        categoria = input("Informe a categoria do produto: ")
        View.inserir_categoria(categoria)

    @staticmethod
    def listar_categoria():
        for categoria in View.listar_categoria():
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
        id = int(input("Informe o id da categoria a ser excluída: "))
        View.excluir_categoria(id)
    

UI.main()
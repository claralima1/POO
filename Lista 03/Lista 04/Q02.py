class Playlist:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []

    def set_nome(self, n):
        self.__nome = n

    def set_descricao(self, d):
        self.__descricao = d

    def set_musicas(self, m):
        self.__musicas = m

    def get_nome(self):
        return self.__nome

    def get_descrição(self):
        return self.__descricao
    
    def get_musicas(self):
        return self.__musicas
    
    def inserir(self):
        self.__musicas.append()
    
    def listar(self):
        return self.__musicas
    
    def __str__(self):
        return f'Nome da música: {self.__musicas}\nDescrição: {self.__descricao}'



class UI:

    def main():
        n = input()
        d = input()
        p = Playlist(n, d)

        print(p)


UI.main()
class Playlist:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []

    def set_nome(self, n):
        self.__nome = n

    def set_descricao(self, d):
        self.__descricao = d

    def get_nome(self):
        return self.__nome

    def get_descrição(self):
        return self.__descricao


    def inserir(self, m):
        self.__musicas.append(m)
    
    def listar(self):
        return self.__musicas
    
    def __str__(self):
        return f'Total de Músicas na Playlist: {len(self.__musicas)}'

class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def __str__(self):
        return f'Título da Música: {self.__titulo} Artista: {self.__artista} Album: {self.__album}'

class UI:

    def main():
        n = input("Nome da Música: ")
        d = input("Descrição: ")
        p = Playlist(n, d)

        print(p)


UI.main()

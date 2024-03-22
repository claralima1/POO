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
    
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    
    def set_artista(self, novo_artista):
        self.__artista = novo_artista
    
    def set_album(self, novo_album):
        self.__album = novo_album
    
    def get_titulo(self):
        return self.__titulo
    
    def get_artista(self):
        return self.__artista

    def get_album(self):
        self.__album

    def __str__(self):
        return f'Título da Música: {self.__titulo} Artista: {self.__artista} Album: {self.__album}'


class UI:

    def main():
      play = None
      op = 0
      while op != 9:
          op = UI.menu()
          if op == 1: 
              play = UI.nova_playlist()
          if op == 2: 
              if play == None: 
                  print("Crie uma nova playlist antes!")
              else:
                  musica = UI.nova_musica()
                  play.inserir(musica)
          if op == 3: 
              if play == None: 
                  print("Crie uma nova playlist antes!")
              else:
                  for musica in play.listar():
                      print(musica)     
    
    def nova_playlist():
      nome = input("Informe o nome da playlist: ")
      desc = input("Informe uma descrição: ")
      playlist = Playlist(nome, desc)
      return playlist
    
    def nova_musica():
      titulo = input("Informe o título da música: ")
      artista = input("Informe o artista ou banda: ")
      album = input("Informe o álbum: ")
      musica = Musica(titulo, artista, album)
      return musica
    
    def menu():
        print("1 - Nova PlayList")
        print("2 - Inserir música")
        print("3 - Listar músicas")
        print("9 - fim")
        return int(input("Opção: "))

UI.main()

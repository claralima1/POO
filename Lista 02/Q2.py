class Viagem:
    def __init__(self, distancia, tempo):
        self.__distancia = distancia
        self.__tempo = tempo

    def set_distancia(self, d):
        if d>=0:
            self.__distancia = d
        else: 
            raise ValueError()

    def set_tempo(self,t):
        if t>=0:
            self.__tempo = t
        else:
            raise ValueError()

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def velocidade_media(self):
        return self.__distancia/self.__tempo

class UI:
    def main():
        x = float(input("Distancia: "))
        y = float(input("Tempo: "))
        v = Viagem(x, y)
        v.set_distancia(x)
        v.set_tempo(y)
        print(v.velocidade_media())
UI.main()

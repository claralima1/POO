class Frete:
    def __init__(self, d, p):
        self.set_distancia(d)
        self.set_peso(p)

    def set_distancia(self, d):
        if d<0:
            raise ValueError()
        else:
            self.__d = d
    def set_peso(self, p):
        if p<0:
            raise ValueError()
        else:
            self.__p = p
    def get_distancia(self):
        return self.__d

    def get_peso(self):
        return self.__p
    
    def Calc_Frete(self):
        return 0.01*self.__p * self.__d
    
    def __str__(self):
        return f'Peso = {self.__p}\nDistância = {self.__d}'

class UI:
    @staticmethod
    def main():
        distancia = float(input("Digite a distância: "))
        peso = float(input("Digite o peso: "))
        f = Frete(distancia, peso)
        print(f)
        print(f'Frete = {f.Calc_Frete()}\n' )
     

UI.main()


class Retangulo:
    def __init__(self, base, altura):
        if base <= 0 :
            raise ValueError
        else:
            self.__base = base
        if altura <=0:
            raise ValueError
        else:
            self.__altura = altura
    def set_base(self, b):
        if b <= 0 :
            raise ValueError
        else:
            self.__base = b

    def set_altura(self, a):
        if a <=0:
            raise ValueError
        else:
            self.__altura = a

    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura

    def __str__(self):
        return f'Base = {self.__base}\nAltura = {self.__altura}'
    
    def calc_area(self):
        return self.__base*self.__altura
    
    def calc_diagonal(self):
        return self.__base**2 + self.__altura**2

  
class UI:
    def main():
        b = float(input("Digite a base do retângulo: "))
        a = float(input("Digite a altura do retângulo: "))
        r = Retangulo(b, a)
        print(f'Area = {r.calc_area()}\nDiagonal = {r.calc_diagonal()}')
        print(r)

UI.main()



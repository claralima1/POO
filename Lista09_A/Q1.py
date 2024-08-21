import math

class Equacao:
    def __init__(self, a, b, c):
        if a<=0: raise ValueError()
        self.__a = a
        if b<=0: raise ValueError()
        self.__b = b
        if c<=0: raise ValueError()
        self.__c = c

    def set_a(self, a):
        if a<=0: raise ValueError()
        self__a = a

    def get_a(self):
        return self.__a
    
    def set_b(self, b):
        if b<=0: raise ValueError()
        self.__b = b

    def get_b(self):
        return self.__b

    def set_c(self, c):
        if c<=0: raise ValueError()
        self.__c = c

    def get_c(self):
        return self.__c
    
    def delta(self):
        c = (self.__b**2) - ((4 * self.__a) * self.__c)
        return c
    
    def Y(self, x):
        y = (self.__a*(x**2)) + (self.__b*x) + self.__c
        return y
    
    def __str__(self):
        return f'Coeficientes:\nA = {self.__a}\nB = {self.__b} \nC = {self.__c}'
    





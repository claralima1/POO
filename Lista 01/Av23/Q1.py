class Disciplina:
    def __init__(self,nome, semestre, media, ch, aprovado):
        nome = self.__nome
        semestre = self.__semestre
        media = self.__media 
        ch = self.__ch
        aprovado = self.__ch

    def set_nome(self, n):
        if self.__nome == " ":
            raise ValueError()
        else: self.__nome = n
        
    def set_semestre(self, s):
        if self.__semestre == " ":
            raise ValueError()
        else: self.__semestre = s

    def set_media(self, m):
        if self.__media == 0:
            raise ValueError()
        else: self.__media = m

    def set_ch(self, ch):
        if self.__ch == 0:
            raise ValueError()
        else: self.__ch = ch

    def set_aprovado(self, a):
        if self.__aprovado == " ":
            raise ValueError()
        else: self.__aprovado = a
    
    def get_nome(self):
        return self.__nome
    
    def get_semestre(self):
        return self.__semestre
    
    def get_media(self):
        return self.__media
    
    def get_ch(self):
        return self.__ch
    
    def get_aprovado(self):
        return self.__aprovado

    def str(self):
        return f'Disciplina: {self.get_nome()} com carga horária de {self.get_ch} Semestre: {self.get_semestre} Média na disciplina: {self.get_media} Situação: {self.get_aprovado}'
    


class Historico:
    def __init(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []
    
    def inserir(self, d):
        self.__disciplina.append(d)

    def Listar(self):
        return self.__disciplinas
    
    def ListarSemestre(self, semestre):
        return self.

    def MaiorMedia():
        maior = 0
        if maior < 
        return 
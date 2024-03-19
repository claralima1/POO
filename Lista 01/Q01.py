class Conta:
	def _init_(self , nome, numero, saldo):
		self.__nome = nome
		self.__numero = numero
		if saldo <=0:
			raise ValueError()
		else:
			self.saldo = saldo

	def saque(self, qtd_saque):
		self.qtd_saque = qtd_saque
		self.novo_saldo = self.saldo - self.qtd_saque
		return self.novo_saldo
	

class UI:
	@staticmethod
	def main():
		nome = input("Digite o nome: ")
		numero = input("Digite o  numero da conta: ")
		saldo = float(input("Digite seu saldo atual: "))
		c = Conta(nome, numero, saldo)
		d = float(input("Digite a quantia do deposito: "))
		s = float(input("Digite a quantia do saque: "))
		#print("saldo com o deposito: ", c.deposito(d))
		print("saldo apos o saque: ", c.saque(s))
UI.main()

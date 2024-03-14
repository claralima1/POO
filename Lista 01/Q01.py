class Conta:
	def _init_(self , nome, numero, saldo):
		self.nome = nome
		self.numero = numero
		self.saldo = saldo
	def deposito(self, qtd):
		self.qtd = qtd
		self.saldo = self.saldo+self.qtd
		return self.saldo
	def saque(self, qtd_saque):
		self.qtd_saque = qtd_saque
		self.saldo = self.saldo - self.qtd_saque
		return self.saldo
n = input("Digite o nome: ")
num = input("Digite o  numero da conta: ")
saldo = float(input("Digite seu saldo atual: "))
d = float(input("Digite a quantia do deposito: "))
s = float(input("Digite a quantia do saque: "))

c = Conta(n, num, saldo)
print("saldo com o deposito: ", c.deposito(d))
print("saldo apos o saque: ", c.saque(s))

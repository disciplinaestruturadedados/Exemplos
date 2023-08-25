class Produto:
	def __init__(self, nome, descricao, valor):
		self.nome = nome
		self.descricao = descricao
		self.valor = valor
		self.valor_imposto = 0.0
	def calcular_valor_imposto(self):
		self.valor_imposto = float(self.valor) * 0.05
		return self.valor_imposto
	def mostra_dados(self):
		print(f'Nome: {self.nome}')
		print(f'Descrição: {self.descricao}')
		print(f'Valor: {self.valor:.2f}')
		print(f'Imposto: {float(self.valor_imposto):.2f}')
		print(f'Valor total a Pagar: {float(self.valor_imposto)+float(self.valor)}')

p1 = Produto('Uva', 'Isabel', 6.00)
p1.calcular_valor_imposto()
p1.mostra_dados()
class Produto:
	def __init__(self, nome, descricao, valor):
		self.nome = nome
		self.descricao = descricao
		self.valor = valor
		self.valor_imposto = 0.0

p1 = Produto('Uva', 'Isabel', '6,00')
print(p1.nome, p1.descricao, p1.valor)
print(p1)
p2 = Produto('Maça', 'Argentina', '8,00')
print(p2.nome, p2.descricao, p2.valor)
print(p2)
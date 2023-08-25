#Questão 3
class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        return a / b

calc = Calculadora()
print(calc.soma(10, 5))
print(calc.subtracao(15, 7))
print(calc.multiplicacao(4, 3))
print(calc.divisao(20, 4))

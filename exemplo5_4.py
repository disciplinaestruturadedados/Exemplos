class Retangulo:
    def calcular_area(self, largura, altura):
        return largura * altura
    
    def calcular_perimetro(self, largura, altura):
        return 2 * (largura + altura)

retangulo = Retangulo()
print(retangulo.calcular_area(5, 3))
print(retangulo.calcular_perimetro(5, 3))
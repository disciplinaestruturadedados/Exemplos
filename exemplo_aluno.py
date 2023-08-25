class Aluno:
    def __init__(self, nome, nota1, nota2):
           self.nome = nome
           self.nota1 = nota1
           self.nota2 = nota2
           self.media = 0.0
    def calcular_media(self):
           self.media = (self.nota1 + self.nota2) / 2
           return self.media
    def mostra_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Nota1: {self.nota1}')
        print(f'Nota2: {self.nota2}')
        print(f'Média: {self.media}')


    def resultado(self):
        if self.media >= 7:
           print('Aluno(a) aprovado (a)')
        else:
           print('Aluno(a) reaprovado (a)')

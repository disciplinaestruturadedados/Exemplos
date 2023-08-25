import time

def somapar(n):
    somapar = 0
    for i in range(n+1):
        if (i%2 == 0):
            somapar = somapar + i
    return somapar

def soma2(n):
    resp=(n * (n + 1)) / 2
    return resp

print(somapar(10))
import time

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma = soma + i
    return soma 

def soma2(n):
    resp=(n * (n + 1)) / 2
    return resp

#Calculando o tempo de execução
inicio=time.time()
resultado=soma1(100000)
termino=time.time()
execution_time = termino - inicio
print(f'O resultao foi de..: {resultado}')
print(f'Tempo de inicio....: {inicio:.5f} segundos')
print(f'Tempo de termino...: {termino:.5f} segundos')
print(f'Tempo de execução..: {execution_time:.10f} segundos')
print('========================================================')
#Calculando o tempo de execução
inicio=time.time()
resultado=soma2(100000)
termino=time.time()
execution_time = termino - inicio
print(f'O resultao foi de..: {resultado}')
print(f'Tempo de inicio: {inicio:.5f} segundos')
print(f'Tempo de termino: {termino:.5f} segundos')
print(f'Tempo de execução: {execution_time:.10f} segundos')
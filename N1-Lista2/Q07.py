print('Digite 5 números: ')
tupla = ()

for i in range(5):
    numeros = input(f'Digite o {i+1}ª numero: ')
    tupla += (numeros,)
    
print(tupla)

primeiroElemento = tupla[0]

print('Retornando ao 1ª elemento da tupla: ', primeiroElemento)
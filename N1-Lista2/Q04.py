conjunto = set()

print('Digite 5 números')

for i in range(5):
    numeros = input(f'Digite o {i+1}ª numero: ')
    conjunto.add(numeros)
    
print(conjunto)

print('Agora escola um dos números digitados para ser removido')

remover = input('Número a ser removido: ')

if remover in conjunto:
    conjunto.remove(remover)
    
print(conjunto)
conjunto = set()

print('Digite 5 números')

for i in range(5):
    numeros = input(f'Digite o {i+1}ª numero: ')
    conjunto.add(numeros) 
    
print(conjunto)

if 3 in conjunto:
    print('O número - 3 - está presente no dicionário')
else:
    print('O número - 3 - não está presente no dicionário')
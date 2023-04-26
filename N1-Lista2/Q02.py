tupla = ()

for i in range(3):
    nomes = input(f'Digite o {i+1}ª nome: ')
    tupla += (nomes,)

print(tupla)
print('Substitua um nome acima')

nomeAntigo = input('Digite o nome que deseja substituir: ')

if nomeAntigo in tupla:
    nomeNovo = input('Digite um novo nome: ')
    
lista = list(tupla)

subs = lista.index(nomeAntigo)
lista[subs] = nomeNovo

tupla = tuple(lista)

print('os nomes atualizados são: ', lista)
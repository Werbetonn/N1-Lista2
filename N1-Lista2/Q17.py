tupla = ()

for i in range(3):
    nums = input(f'Digite o {i+1}ª nome: ')
    tupla += (nums,)
    
print(tupla)

quantTupla = tupla.count('Maria' or 'maria')

print(f'O nome Maria aparece {quantTupla} vez(es) na tupla')
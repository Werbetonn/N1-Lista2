lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

pares = []
for i in range(len(lista)):
    if i % 2 == 0:
        pares.append(lista[i])

print("Elementos de índice par da lista:")
for elemento in pares:
    print(elemento)
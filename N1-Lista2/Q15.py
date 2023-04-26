grafo = {}

vertices = input("Digite os vértices do grafo separados por espaço: ").split()

arestas = set()

while True:
    aresta = input("Digite uma aresta do grafo (ou digite 'fim' para encerrar): ")
    if aresta == "fim":
        break
    else:
        aresta = tuple(aresta.split())
        if len(aresta) != 2 or aresta[0] not in vertices or aresta[1] not in vertices:
            print("Aresta inválida! Digite novamente.")
        else:
            arestas.add(aresta)

for v in vertices:
    grafo[v] = set()

for u, v in arestas:
    grafo[u].add(v)
    grafo[v].add(u)

if ('A', 'C') in arestas:
    print("A aresta ('A', 'C') está presente no grafo!")
else:
    print("A aresta ('A', 'C') não está presente no grafo.")
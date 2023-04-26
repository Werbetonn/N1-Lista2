grafo = {}

ver1 = input("Digite os vértices: ").split()

for ver2 in ver1:
    grafo[ver2] = []

a = input("Digite as arestas: ").split(",")

for a in a:
    v1, v2 = a.strip().split()
    grafo[v1].append(v2)
    grafo[v2].append(v1)
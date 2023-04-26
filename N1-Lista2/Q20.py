grafo = {}

grafo['A'] = []
grafo['B'] = []
grafo['C'] = []
grafo['D'] = []

grafo['A'].append('B')
grafo['B'].append('A')
grafo['B'].append('C')
grafo['C'].append('B')
grafo['C'].append('D')
grafo['D'].append('C')

print(grafo)
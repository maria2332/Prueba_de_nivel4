# import networkx as nx

# # Creamos el grafo
# G = nx.Graph()

# # Definimos los nombres de los personajes
# personajes = ["Iron Man", "The increíble Hulk", "Khan", "Thor", "Captain América", "Ant-Man", "Nick Fury", "The Winter Soldier"]

# # Agregamos los nodos al grafo
# for personaje in personajes:
#     G.add_node(personaje)

# # Definimos la matriz de adyacencia
# matriz = [[6, 0, 1, 8, 7, 3, 2, 0],
#           [6, 0, 6, 1, 8, 9, 1, 0],
#           [0, 0, 0, 1, 2, 1, 5, 0],
#           [1, 6, 1, 0, 1, 5, 9, 3],
#           [8, 1, 2, 1, 0, 2, 4, 5],
#           [7, 8, 1, 5, 2, 0, 1, 6],
#           [3, 9, 5, 9, 4, 1, 0, 1],
#           [2, 1, 0, 3, 5, 6, 1, 0]]

# # Agregamos las aristas al grafo
# for i in range(len(personajes)):
#     for j in range(i, len(personajes)):
#         if matriz[i][j] > 0:
#             G.add_edge(personajes[i], personajes[j], weight=matriz[i][j])

# # Definimos los vértices de inicio
# inicio = ["Iron Man", "Thor", "The Winter Soldier"]

# # Buscamos los nodos conectados a los vértices de inicio
# conectados = set()
# for v in inicio:
#     conectados |= set(nx.dfs_tree(G, v).nodes())

# # Aplicamos el algoritmo de Kruskal para encontrar el árbol de expansión máximo
# T = nx.algorithms.tree.maximum_spanning_tree(G.subgraph(conectados), algorithm='kruskal')

# characters = ['Iron Man', 'The increíble Hulk', 'Khan', 'Thor', 'Captain América', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']

# # Imprimimos los nombres de los personajes en el árbol de expansión máximo
# for u, v in T.edges():
#     print(u, "-", v)

# # Recorremos la matriz y encontramos el valor máximo que no sea infinito
# max_episodes = -1
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] != float('inf') and matriz[i][j] > max_episodes:
#             max_episodes = matriz[i][j]

# # Recorremos la matriz nuevamente y obtenemos los pares de personajes que coinciden con el número máximo de episodios
# pairs = []
# for i in range(len(matriz)):
#     for j in range(i+1, len(matriz[i])):
#         if matriz[i][j] == max_episodes:
#             pairs.append((characters[i], characters[j]))

# # Imprimimos los resultados
# print(f"El número máximo de episodios compartidos por dos personajes es {max_episodes}.")
# print("Los pares de personajes que coinciden con dicho número son:")
# for pair in pairs:
#     print(f"{pair[0]} y {pair[1]}")

# adjacency_matrix = [
#     [6, 0, 1, 8, 7, 3, 2, 6],
#     [0, 6, 0, 6, 9, 1, 9, 0],
#     [1, 0, 0, 1, 2, 1, 5, 1],
#     [8, 6, 1, 0, 1, 5, 9, 3],
#     [7, 9, 2, 1, 0, 2, 4, 5],
#     [3, 1, 1, 5, 2, 0, 1, 6],
#     [2, 9, 5, 9, 4, 1, 0, 1],
#     [6, 0, 1, 3, 5, 6, 1, 0]
# ]

# # Crear un diccionario para contar el número de veces que cada personaje aparece en una arista
# appearance_count = {}
# for i in range(len(characters)):
#     appearance_count[characters[i]] = 0
#     for j in range(i, len(characters)):
#         if i == j:
#             appearance_count[characters[i]] += adjacency_matrix[i][j]
#         else:
#             appearance_count[characters[i]] += adjacency_matrix[i][j]
#             appearance_count[characters[j]] += adjacency_matrix[i][j]

# # Identificar los personajes que aparecen en nueve aristas
# characters_with_nine_appearances = []
# for character, count in appearance_count.items():
#     if count == 9:
#         characters_with_nine_appearances.append(character)

# print("Los siguientes personajes aparecieron en nueve episodios de la saga:")
# print(characters_with_nine_appearances)

import numpy as np
from heapq import heappop, heappush

# Nombres de los personajes
personajes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']

# Matriz de adyacencia
grafo = np.array([
  [0, 6, 0, 1, 8, 7, 3, 2],
  [6, 0, 0, 6, 1, 8, 9, 1],
  [0, 0, 0, 1, 2, 1, 5, 0],
  [1, 6, 1, 0, 1, 5, 9, 3],
  [8, 1, 2, 1, 0, 2, 4, 5],
  [7, 8, 1, 5, 2, 0, 1, 6],
  [3, 9, 5, 9, 4, 1, 0, 1],
  [2, 1, 0, 3, 5, 6, 1, 0]
])

# Algoritmo de Prim
def prim(grafo, inicio):
    n = len(grafo)
    visitados = [False]*n
    pesos = [-1]*n
    previos = [None]*n
    pesos[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        peso, u = heappop(cola_prioridad)
        if not visitados[u]:
            visitados[u] = True
            for v, peso_uv in enumerate(grafo[u]):
                if not visitados[v] and (pesos[v] == -1 or pesos[v] < peso_uv):
                    pesos[v] = peso_uv
                    previos[v] = u
                    heappush(cola_prioridad, (peso_uv, v))
    return previos

# Apartado a
print("\n")
print("\nApartado b:")
inicio = personajes.index('Iron Man')
previos = prim(grafo, inicio)
print("Árbol de expansión máximo desde Iron Man:")
for i, p in enumerate(previos):
    if p is not None:
        print(f'{personajes[p]} -- {personajes[i]}')

# Apartado b
print("\n")
print("\nApartado c:")
max_episodios = np.max(grafo)
print(f'\nMáximo número de episodios compartidos: {max_episodios}')
print('Pares de personajes que comparten el máximo número de episodios:')
indices = np.where(grafo == max_episodios)
for i in range(len(indices[0])):
    if indices[0][i] < indices[1][i]:
        print(f'{personajes[indices[0][i]]} -- {personajes[indices[1][i]]}')

# Apartado c
print("\n")
print("\nApartado d:")
print('\nTodos los personajes:')
for personaje in personajes:
    print(personaje)

# Apartado d
print("\n")
print("\nApartado e:")
print('\nPersonajes que aparecieron en nueve episodios de la saga:')
indices_nueve_episodios = np.where(grafo == 9)
for i in range(len(indices_nueve_episodios[0])):
    if indices_nueve_episodios[0][i] < indices_nueve_episodios[1][i]:
        print(f'{personajes[indices_nueve_episodios[0][i]]} -- {personajes[indices_nueve_episodios[1][i]]}')
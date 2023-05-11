import networkx as nx

# Creamos el grafo
G = nx.Graph()

# Definimos los nombres de los personajes
personajes = ["Iron Man", "The increíble Hulk", "Khan", "Thor", "Captain América", "Ant-Man", "Nick Fury", "The Winter Soldier"]

# Agregamos los nodos al grafo
for personaje in personajes:
    G.add_node(personaje)

# Definimos la matriz de adyacencia
matriz = [[6, 0, 1, 8, 7, 3, 2, 0],
          [6, 0, 6, 1, 8, 9, 1, 0],
          [0, 0, 0, 1, 2, 1, 5, 0],
          [1, 6, 1, 0, 1, 5, 9, 3],
          [8, 1, 2, 1, 0, 2, 4, 5],
          [7, 8, 1, 5, 2, 0, 1, 6],
          [3, 9, 5, 9, 4, 1, 0, 1],
          [2, 1, 0, 3, 5, 6, 1, 0]]

# Agregamos las aristas al grafo
for i in range(len(personajes)):
    for j in range(i, len(personajes)):
        if matriz[i][j] > 0:
            G.add_edge(personajes[i], personajes[j], weight=matriz[i][j])

# Definimos los vértices de inicio
inicio = ["Iron Man", "Thor", "The Winter Soldier"]

# Buscamos los nodos conectados a los vértices de inicio
conectados = set()
for v in inicio:
    conectados |= set(nx.dfs_tree(G, v).nodes())

# Aplicamos el algoritmo de Kruskal para encontrar el árbol de expansión máximo
T = nx.algorithms.tree.maximum_spanning_tree(G.subgraph(conectados), algorithm='kruskal')

# Imprimimos los nombres de los personajes en el árbol de expansión máximo
for u, v in T.edges():
    print(u, "-", v)

# Recorremos la matriz y encontramos el valor máximo que no sea infinito
max_episodes = -1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != float('inf') and matrix[i][j] > max_episodes:
            max_episodes = matrix[i][j]

# Recorremos la matriz nuevamente y obtenemos los pares de personajes que coinciden con el número máximo de episodios
pairs = []
for i in range(len(matrix)):
    for j in range(i+1, len(matrix[i])):
        if matrix[i][j] == max_episodes:
            pairs.append((characters[i], characters[j]))

# Imprimimos los resultados
print(f"El número máximo de episodios compartidos por dos personajes es {max_episodes}.")
print("Los pares de personajes que coinciden con dicho número son:")
for pair in pairs:
    print(f"{pair[0]} y {pair[1]}")

    characters = ['Iron Man', 'The increíble Hulk', 'Khan', 'Thor', 'Captain América', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']


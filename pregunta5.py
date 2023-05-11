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

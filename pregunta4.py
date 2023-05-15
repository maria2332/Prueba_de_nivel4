import itertools

# Matriz de distancias
distancias = [
    [0, 675, 400, 166, 809, 720, 399, 233],
    [675, 0, 540, 687, 179, 348, 199, 401],
    [400, 540, 0, 107, 752, 521, 385, 280],
    [166, 687, 107, 0, 111, 540, 990, 361],
    [809, 179, 752, 111, 0, 206, 412, 576],
    [720, 348, 521, 540, 206, 0, 155, 621],
    [399, 199, 385, 990, 412, 155, 0, 100],
    [233, 401, 280, 361, 576, 621, 100, 0]
]

heroes = ["Iron Man", "The Incredible Hulk", "Khan", "Thor", "Captain America", "Ant-Man", "Nick Fury", "The Winter Soldier"]

# Calcula la longitud total de la ruta
def calcular_ruta(ruta):
    return sum(distancias[i][j] for i, j in zip(ruta, ruta[1:] + ruta[:1]))

# Genera todas las rutas posibles
rutas = list(itertools.permutations(range(8)))

# Encuentra la ruta más corta
ruta_minima = min(rutas, key=calcular_ruta)

# Imprime la ruta más corta
print("La ruta más corta es:")
for i in ruta_minima:
    print(heroes[i])
print("Con una longitud total de:", calcular_ruta(ruta_minima))
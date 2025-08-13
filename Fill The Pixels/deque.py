from collections import deque


def bfs(start_x, start_y, moves, grid, visited, w, h):
    cola = deque()

    cola.append((start_x, start_y)) 
    # añadimos x e y iniciales a la cola deque.
    # x, y son la ubicacion del nodo padre (nodo del cual expandimos)

    
    # cola registra nodo padre
    visited[start_y][start_x] = True

    while cola:
        x, y = cola.popleft() # extraemos al nodo padre de la cola

        for movX, movY in moves: #coordenadas de las tuplas en lista.

            nx, ny = x + movX, y + movY
            # la ubicacion exacta calculado la coordenada del padre
            # + la coordenada del movimiento

            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx] and grid[ny][nx] == 1:
                    visited [ny][nx] = True
                    cola.append((nx, ny)) # si existen vecinos, los ponemos en la cola




def min_clicks_brush(moves, grid, w, h):
    """Numero de clicks para moves en grid (dimensiones w, h)"""

    visited = [[False] * w for _ in range(h)]

    clicks = 0

    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1 and not visited[y][x]:
                #encontramos nodo no visitado y ejecutamos bfs

                bfs(x, y, moves, grid, visited, w, h)
                clicks += 1
    
    return clicks


# MAIN 


t = int(input().strip())

plus_m = [(-1, 0), (1, 0), (0, 1), (0, -1)]
cross_m = [(-1,-1), (-1,1), (1,-1), (1,1)] 
start_m = plus_m + cross_m # Es decir, todas las direcciones de los anteriores

for _ in range(t):
    w, h = map(int, input().split())

    grid = [[int(ch) for ch in input().strip()] for _ in range(h)]

    plus_clicks = min_clicks_brush(plus_m, grid, w, h)
    cross_clicks = min_clicks_brush(cross_m, grid, w, h)
    star_clicks = min_clicks_brush(start_m, grid, w, h)

    print(plus_clicks, cross_clicks, star_clicks)



# Fill The Pixels Docs

## Standard output
For each test case output, 3 space separated integers which denote the minimum number of clicks needed to clear out the picture for each of the three brushes: +, x and *.

## Recursos utilizados:
- Python 3
  - De Collections
    - Deque: Funciona como una lista, con funciones identicas, pero que se permite trabajar desde ambos sentidos. Eso es util para BFS debido a como gestiona pop python, lo cual hace mucho trabajo al mover los elementos.
- BFS: Busqueda por anchura. Permite recorrer todos los nodos y sus vecinos guardados en una cola (deque) hasta que no hayan mas vecinos.

## Desarrollo del Algoritmo
Dado (1) un numero determinado de matrices, y de cada una (2) dadas las dimensiones (w, h -> ancho, alto) de cada elemento o "nodo" de la matriz existen dos posibles valores, 1 o 0.
El objetivo es encontrar la mínima cantidad de "clicks" necesarios para cubrir todos los píxeles blancos (valor 1) usando exclusivamente cada tipo de pincel (brush):

- Brush + (plus): conecta los píxeles arriba, abajo, izquierda y derecha (4)

- Brush x (cross): conecta los píxeles en las diagonales (4).

- Brush * (star): conecta los píxeles en las 8 direcciones (8).

Cada brush tiene un conjunto de movimientos que se pueden representar como una unidad al lado en cualquier sentidos para los valores de w, h.

Cada "click" representa seleccionar un píxel blanco no visitado y usar el pincel para cubrir toda la componente conectada que abarca, según la conectividad definida por el pincel. Sin embargo, cada uno de los vecinos afectados repiten el mismo efecto del pincel, lo cual provoca un bucle o recursion.
**Esto se efectua en la funcion *min_clicks_brush*.**

Partiendo de un píxel blanco no visitado, se hace una búsqueda por anchura (BFS) para recorrer todos sus vecinos conectados (según movimientos permitidos por el pincel) y marcarlos como visitados. BFS registra todos los vecinos en una cola que permite iterar sobre cada vecino.
Se repite el proceso hasta que todos los píxeles blancos estén visitados. 
**Esto se efectua en la funcion *bfs*.**

Se mantiene una matriz visited para evitar procesar varias veces el mismo píxel, esta matriz es identica a la matriz original y registra todas las visitas y clicks para evitar operar un elemento que pudo haber sido ya visitado mas no clickeado. 

---

>El número de veces que se inicia BFS corresponde a la cantidad mínima de clicks necesarios.






"""
===========================================================
Archivo: grafo.py

Descripción:
-------------
Este archivo representa el MODELO del proyecto.

Aquí se almacena el grafo utilizando una Lista de Adyacencia.

También contiene métodos para:

- Agregar nodos
- Agregar aristas
- Obtener vecinos
- Mostrar el grafo

Los algoritmos BFS, DFS y Dijkstra estarán en archivos
separados para mantener el código organizado.
===========================================================
"""


class Grafo:
    """
    Clase que representa un grafo dirigido y con pesos.
    """

    def __init__(self):
        """
        Constructor de la clase.

        Crea un diccionario vacío donde se almacenará
        el grafo mediante lista de adyacencia.

        Estructura:

        {
            "A":[("B",5),("C",2)],
            "B":[("D",4)]
        }
        """

        self.grafo = {}

    # -----------------------------------------------------

    def agregar_nodo(self, nodo):
        """
        Agrega un nodo al grafo.

        Parámetros
        ----------
        nodo : str

        Retorna
        -------
        None
        """

        if nodo not in self.grafo:
            self.grafo[nodo] = []

    # -----------------------------------------------------

    def agregar_arista(self, origen, destino, peso):
        """
        Agrega una conexión entre dos nodos.

        Parámetros
        ----------
        origen : str

        destino : str

        peso : int

        Retorna
        -------
        None
        """

        # Si los nodos no existen, los crea.

        self.agregar_nodo(origen)
        self.agregar_nodo(destino)

        # Agrega la conexión si no existe un arco hacia el mismo destino.
        if not any(vecino == destino for vecino, _ in self.grafo[origen]):
            self.grafo[origen].append((destino, peso))

    # -----------------------------------------------------

    def obtener_vecinos(self, nodo):
        """
        Devuelve todos los vecinos de un nodo.

        Parámetros
        ----------
        nodo : str

        Retorna
        -------
        list
        """

        return self.grafo.get(nodo, [])

    # -----------------------------------------------------

    def obtener_nodos(self):
        """
        Devuelve todos los nodos del grafo.

        Retorna
        -------
        list
        """

        return list(self.grafo.keys())

    # -----------------------------------------------------

    def obtener_grafo(self):
        """
        Devuelve todo el grafo.

        Retorna
        -------
        dict
        """

        return self.grafo

    # -----------------------------------------------------

    def obtener_todas_rutas_desde(self, origen):
        """
        Devuelve todas las rutas simples (sin ciclos) que parten
        desde el nodo `origen` hacia cualquier nodo alcanzable.

        Retorna
        -------
        list
            Lista de tuplas: (ruta_lista, peso_total). Ejemplo:
            (["Restaurante", "A", "B"], 12)
        """

        if origen not in self.grafo:
            return []

        rutas = []

        def _dfs(actual, camino, peso_acumulado):
            for vecino, peso in self.grafo.get(actual, []):
                if vecino in camino:
                    continue

                nuevo_camino = camino + [vecino]
                nuevo_peso = peso_acumulado + peso

                rutas.append((nuevo_camino, nuevo_peso))

                # Seguir profundizando desde el vecino
                _dfs(vecino, nuevo_camino, nuevo_peso)

        _dfs(origen, [origen], 0)

        return rutas

    # -----------------------------------------------------

    def mostrar_grafo(self):
        """
        Imprime el grafo en consola.

        Solo se utiliza para depuración.
        """

        print("\n===== GRAFO =====\n")

        for nodo in self.grafo:

            print(f"{nodo} -> {self.grafo[nodo]}")

    # -----------------------------------------------------

    def eliminar_nodo(self, nodo):
        """
        Elimina un nodo del grafo y todas sus conexiones.

        Parámetros
        ----------
        nodo : str

        Retorna
        -------
        None
        """

        if nodo not in self.grafo:
            return

        # Elimina el nodo
        del self.grafo[nodo]

        # Elimina todas las conexiones hacia este nodo
        for n in self.grafo:
            self.grafo[n] = [(destino, peso) for destino, peso in self.grafo[n] if destino != nodo]

    # -----------------------------------------------------

    def limpiar_grafo(self):
        """
        Elimina todos los nodos del grafo.

        Retorna
        -------
        None
        """

        self.grafo = {}

"""
===========================================================
Archivo: panel_grafo.py

Descripción:
-------------
Este módulo se encarga EXCLUSIVAMENTE de dibujar el grafo.

Responsabilidades:
- Dibujar nodos
- Dibujar aristas
- Mostrar pesos
- Resaltar rutas (BFS/DFS/Dijkstra)
===========================================================
"""

import tkinter as tk


class PanelGrafo:

    def __init__(self, parent):

        self.canvas = tk.Canvas(
            parent,
            bg="white",
            width=700,
            height=500
        )

        self.canvas.pack(fill="both", expand=True)

        # posiciones fijas de nodos
        self.posiciones = {}

    # ------------------------------------------------------

    def set_posiciones(self, posiciones):
        """
        Guarda posiciones de los nodos.
        """
        self.posiciones = posiciones

    # ------------------------------------------------------

    def limpiar(self):
        """
        Limpia el canvas.
        """
        self.canvas.delete("all")

    # ------------------------------------------------------

    def dibujar(self, grafo):
        """
        Dibuja todo el grafo.
        """

        self.limpiar()

        # ARISTAS
        aristas_vistas = set()

        for origen in grafo:
            if origen not in self.posiciones:
                continue

            x1, y1 = self.posiciones[origen]

            for destino, peso in grafo[origen]:

                if destino not in self.posiciones:
                    continue

                x2, y2 = self.posiciones[destino]

                # Acortar la línea para que no atraviese el nodo destino
                radio_nodo = 24
                dx = x2 - x1
                dy = y2 - y1
                distancia = (dx * dx + dy * dy) ** 0.5
                
                if distancia > 0:
                    # Calcular punto donde termina la línea (antes del nodo)
                    x2_acortado = x2 - (dx / distancia) * radio_nodo
                    y2_acortado = y2 - (dy / distancia) * radio_nodo
                else:
                    x2_acortado = x2
                    y2_acortado = y2

                # línea con flecha - TODO NEGRO
                self.canvas.create_line(
                    x1, y1, x2_acortado, y2_acortado,
                    fill="black",
                    width=3,
                    arrow=tk.LAST,
                    arrowshape=(12, 15, 6)
                )

                pareja = tuple(sorted((origen, destino)))
                if pareja not in aristas_vistas:
                    aristas_vistas.add(pareja)

                    # peso - mejor posicionado
                    px = (x1 + x2) / 2
                    py = (y1 + y2) / 2

                    dx_pos = x2 - x1
                    dy_pos = y2 - y1
                    longitud = (dx_pos * dx_pos + dy_pos * dy_pos) ** 0.5

                    if longitud > 0:
                        nx = -dy_pos / longitud
                        ny = dx_pos / longitud
                        offset = 20  # Mayor offset para mejor visibilidad
                        px += nx * offset
                        py += ny * offset
                    else:
                        px += 10
                        py -= 10

                    rect_x1 = px - 16
                    rect_y1 = py - 11
                    rect_x2 = px + 16
                    rect_y2 = py + 11

                    # Fondo blanco con borde y texto negro
                    self.canvas.create_rectangle(
                        rect_x1, rect_y1, rect_x2, rect_y2,
                        fill="white",
                        outline="black",
                        width=2
                    )

                    self.canvas.create_text(
                        px,
                        py,
                        text=str(peso),
                        fill="black",
                        font=("Arial", 10, "bold"),
                        anchor="center",
                        tags="peso"
                    )

        # NODOS
        for nodo, (x, y) in self.posiciones.items():

            radio = 24
            self.canvas.create_oval(
                x - radio, y - radio,
                x + radio, y + radio,
                fill="lightblue",
                outline="black",
                width=2
            )

            self.canvas.create_text(
                x, y,
                text=nodo,
                font=("Arial", 11, "bold")
            )

    # ------------------------------------------------------

    def resaltar_ruta(self, ruta):
        """
        Resalta la ruta en rojo.
        """

        if not ruta:
            return

        for i in range(len(ruta) - 1):

            a = ruta[i]
            b = ruta[i + 1]

            if a not in self.posiciones or b not in self.posiciones:
                continue

            x1, y1 = self.posiciones[a]
            x2, y2 = self.posiciones[b]

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill="red",
                width=4,
                arrow=tk.LAST
            )
"""
===========================================================
Test: Comparación BFS vs DFS
===========================================================

Este archivo compara visualmente los recorridos de
BFS y DFS en el grafo del proyecto.
"""

from models.grafo import Grafo
from models.bfs import BFS
from models.dfs import DFS
from utils.lector_json import LectorJSON


def main():
    """
    Ejecuta pruebas comparativas de BFS y DFS.
    """
    
    # Cargar el grafo desde JSON
    lector = LectorJSON()
    grafo_dict = lector.cargar("data/mapa.json")
    
    # Crear instancia del grafo
    grafo = Grafo()
    
    # Llenar el grafo con los datos del JSON
    for origen, destinos in grafo_dict.items():
        grafo.agregar_nodo(origen)
        for destino, peso in destinos:
            grafo.agregar_arista(origen, destino, peso)
            # Hacer el grafo BIDIRECCIONAL (como en la app)
            if origen != destino:
                grafo.agregar_arista(destino, origen, peso)
    
    # Mostrar el grafo
    print("=" * 60)
    print("GRAFO CARGADO:")
    print("=" * 60)
    for nodo, vecinos in grafo.grafo.items():
        print(f"\n{nodo}:")
        for vecino, peso in vecinos:
            print(f"  → {vecino} (peso: {peso})")
    
    # Ejecutar BFS
    print("\n" + "=" * 60)
    print("BFS - BREADTH FIRST SEARCH (Por amplitud)")
    print("=" * 60)
    bfs = BFS()
    recorrido_bfs = bfs.recorrer(grafo.grafo, "Restaurante")
    print(f"\nOrigen: Restaurante")
    print(f"Recorrido: {' → '.join(recorrido_bfs)}")
    print(f"Orden: {recorrido_bfs}")
    
    # Ejecutar DFS
    print("\n" + "=" * 60)
    print("DFS - DEPTH FIRST SEARCH (Por profundidad)")
    print("=" * 60)
    dfs = DFS()
    recorrido_dfs = dfs.recorrer(grafo.grafo, "Restaurante")
    print(f"\nOrigen: Restaurante")
    print(f"Recorrido: {' → '.join(recorrido_dfs)}")
    print(f"Orden: {recorrido_dfs}")
    
    # Comparación
    print("\n" + "=" * 60)
    print("COMPARACIÓN:")
    print("=" * 60)
    print(f"\n✓ BFS encuentra CAMINO MÁS CORTO (por cantidad de saltos)")
    print(f"✓ DFS explora PROFUNDAMENTE una rama antes de retroceder")
    print(f"\nBFS: {len(recorrido_bfs)} nodos visitados")
    print(f"DFS: {len(recorrido_dfs)} nodos visitados")
    print(f"\n¿Son iguales? {recorrido_bfs == recorrido_dfs}")
    
    # Pruebas con diferentes orígenes
    print("\n" + "=" * 60)
    print("PRUEBAS CON DIFERENTES ORÍGENES:")
    print("=" * 60)
    
    origenes = ["Restaurante", "A", "B", "C"]
    
    for origen in origenes:
        if origen in grafo.grafo:
            print(f"\n--- Desde: {origen} ---")
            bfs_recorrido = bfs.recorrer(grafo.grafo, origen)
            dfs_recorrido = dfs.recorrer(grafo.grafo, origen)
            print(f"BFS: {' → '.join(bfs_recorrido)}")
            print(f"DFS: {' → '.join(dfs_recorrido)}")


if __name__ == "__main__":
    main()

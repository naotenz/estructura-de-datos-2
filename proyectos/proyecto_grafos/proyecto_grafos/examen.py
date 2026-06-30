from models.grafo import Grafo
from models.bfs import BFS
from models.dfs import DFS
from utils.lector_json import LectorJSON


def main():
    lector = LectorJSON()
    grafo_dict = lector.cargar("data/mapa.json")
    
    
    grafo = Grafo()
    
    
    for origen, destinos in grafo_dict.items():
        grafo.agregar_nodo(origen)
        for destino, peso in destinos:
            grafo.agregar_arista(origen, destino, peso)
            
            if origen != destino:
                grafo.agregar_arista(destino, origen, peso)

    bfs = BFS()
    

    origenes = ["Restaurante"]

    for origen in origenes:
        if origen in grafo.grafo:
            print(f"\n--- Desde: {origen} ---")
            bfs_recorrido = bfs.recorrer(grafo.grafo, origen)
            
            print(f"BFS: {' → '.join(bfs_recorrido)}")
            
            # Mostrar todas las rutas simples desde el origen con su peso total
            print("\nRutas posibles desde el origen (ruta : peso):")
            rutas = grafo.obtener_todas_rutas_desde(origen)
            if not rutas:
                print("  (No hay rutas)")
            else:
                for ruta, peso in rutas:
                    print(f"  {' → '.join(ruta)} : {peso}")

                # Encontrar la ruta de menor peso
                ruta_mas_corta = min(rutas, key=lambda x: x[1])
                ruta_str = ' → '.join(ruta_mas_corta[0])
                print(f"\nRuta más corta (por peso): {ruta_str} : {ruta_mas_corta[1]}")
            

    
    

if __name__ == "__main__":
    main()
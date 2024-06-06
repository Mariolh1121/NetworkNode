"""
k.py: Script para obtener la conectividad de un nodo
Este script consulta la longitud de la lista de nodos asociados a otro nodo 

Uso:
    python k.py <path_del_archivo_de_interacciones> <nodo_del_que_se_requiera_la_conectividad>

Argumentos:
    <path_del_archivo_de_interacciones> <nodo_del_que_se_requiera_la_conectividad>
"""

import argparse
import sys

network_lib_path = r'C:\Users\mario\OneDrive\Escritorio\Mario\CienciasGenomicas\Primero\SegundoSemestre\Python\NetworkNode'
sys.path.append(network_lib_path)

from NodeNetworklib.operations import Red
def main():
    parser = argparse.ArgumentParser(description="Plotea la gráfica de P(k) de una red de interacciones.")
    parser.add_argument("file", type=str, help="Archivo de lista de interacciones de genes.")
    parser.add_argument("nodo", type=str, help="Nodo del que se requiera la conectividad.")
  
    args = parser.parse_args()
    file_path = args.file
    nodo = args.nodo

    try:
        red = Red(file_path)
        k = red.k(nodo)
        print("Red creada correctamente.")
        print(f"Nodo: {nodo}")
        k = red.k(nodo)
        if k is not None:
            print(f"La conectividad del nodo ingre es {k}")
        else:
            print(f"El nodo '{nodo}' no existe en la red.")
    except Exception as e:
        print(f"Error, archivo no encontrado: ")

if __name__ == "__main__":
    main()
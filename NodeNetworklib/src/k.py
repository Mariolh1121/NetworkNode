"""
k.py: Script para obtener la conectividad de un nodo
Este script consulta la longitud de la lista de nodos asociados a otro nodo 

Uso:
    python k.py <path_del_archivo_de_interacciones> <nodo_del_que_se_requiera_la_conectividad>

Argumentos:
    <path_del_archivo_de_interacciones> <nodo_del_que_se_requiera_la_conectividad>
"""

import argparse
from NodeNetworklib.operations.Network import Red

def main():
    parser = argparse.ArgumentParser(description="Plotea la gráfica de P(k) de una red de interacciones.")
    parser.add_argument("file", type=str, help="Archivo de lista de interacciones de genes.")
    parser.add_argument("nodo", type=str, help="Nodo del que se requiera la conectividad.")
  
    args = parser.parse_args()
    file_path = args.file
    nodo = args.nodo

    try:
        red = Red(file_path)
        print(red.k(nodo))
    except Exception as e:
        print(f"Error, archivo no encontrado: ")

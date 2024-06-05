"""
ck.py: Script para obtener coeficiente de clustering de un nodo
Este script conseguigue los vecinos de un nodo, hace la suma de las
conexiones que hay entre los vecinos de cada uno de los vecinos y lo
divide entre la conectividad máxima del nodo

Uso:
    python ck.py <path_del_archivo_de_interacciones> <nodo_del_que_se_requiere_el_ck>
Argumentos:
    <path_del_archivo_de_interacciones> <nodo_del_que_se_requiere_el_ck>
"""

import argparse
import sys
network_lib_path = r'C:\Users\mario\OneDrive\Escritorio\Mario\CienciasGenomicas\Primero\SegundoSemestre\Python\NetworkNode'
sys.path.append(network_lib_path)

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
        print(red.ck(nodo))
    except Exception as e:
        print(f"Error, archivo no encontrado: ")

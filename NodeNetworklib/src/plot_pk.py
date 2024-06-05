"""
plot_pk.py: Script para plotear la probabilidad de que dada una conectividad "k" aparezca en la red

Este script lee una lista de interacciones dada un archivo, posteriormente guarda los grados de cada nodo
en una lista y calcula la frecuencia que aparece esa conectividad. Finalemnte crea un plot de esa conectividad de manera
normal y logaritmica.

Uso:
    python plot_pk.py <path_del_archivo_de_interacciones>

Argumentos:
    <path_del_archivo_de_interacciones> : Ruta al archivo de texto que contenga la lista de interacciones.
"""

import argparse
import sys

network_lib_path = r'C:\Users\mario\OneDrive\Escritorio\Mario\CienciasGenomicas\Primero\SegundoSemestre\Python\NetworkNode'
sys.path.append(network_lib_path)

from NodeNetworklib.operations.Network import Red

def main():
    parser = argparse.ArgumentParser(description="Plotea la gráfica de P(k) de una red de interacciones.")
    parser.add_argument("file", type=str, help="Archivo de lista de interacciones de genes.")

    args = parser.parse_args()
    file_path = args.file
    try:
        red = Red(file_path)
        red.plot_pk()
    except Exception as e:
        print(f"Error, archivo no encontrado: ")

if __name__ == "__main__":
    main()
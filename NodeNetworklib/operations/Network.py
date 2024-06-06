import matplotlib.pyplot as plt
import numpy as np

class Red:
    """
    Clase que representa una red de interacciones entre nodos.

    Esta clase permite cargar un archivo de interacciones, calcular diversas métricas de la red
    y realizar gráficos para visualizar la distribución de las conectividades.

    Atributos:
    - archivo (str): Ruta al archivo de interacciones.
    - red (dict): Diccionario que almacena las interacciones de la red, donde las claves son los nodos
                  y los valores son listas de tuplas que representan las conexiones con otros nodos.

    Métodos:
    - __init__(archivo): Constructor de la clase, recibe la ruta al archivo de interacciones y carga los datos.
    - cargar_archivo(): Método privado que carga las interacciones desde el archivo especificado.
    - k(nodo): Calcula la conectividad del nodo especificado.
    - ck(nodo): Calcula el coeficiente de clustering del nodo especificado.
    - plot_ck(): Grafica el coeficiente de clustering en función de la conectividad de los nodos.
    - plot_pk(): Grafica la distribución de probabilidad de conectividad de los nodos.
    """

    def __init__(self, archivo):
        """
        Inicializa una instancia de la clase Red.

        Parámetros:
        - archivo (str): Ruta al archivo de interacciones.
        """
        self.archivo = archivo
        self.cargar_archivo()

    def cargar_archivo(self):
        """
        Carga las interacciones desde el archivo especificado.
        """
        self.red = {}
        with open(self.archivo, 'r') as regulacion:
            lineas = regulacion.readlines()[1:]
            for linea in lineas:
                regulador, regulado, efecto = linea.strip().split('\t')
                if regulador != regulado:
                    if regulador not in self.red:
                        self.red[regulador] = []
                        self.red[regulador].append((regulado, efecto))
                    else:
                        self.red[regulador].append((regulado, efecto))
                    if regulado not in self.red:
                        self.red[regulado] = []
                        self.red[regulado].append((regulador, efecto))
                    else:
                        self.red[regulado].append((regulador, efecto))

    def k(self, nodo):
        """
        Calcula la conectividad del nodo especificado.

        Parámetros:
        - nodo (str): Nodo del que se desea calcular la conectividad.

        Retorna:
        - int: Conectividad del nodo.
        """
        return len(self.red.get(nodo, []))

    def ck(self, nodo):
        """
        Calcula el coeficiente de clustering del nodo especificado.

        Parámetros:
        - nodo (str): Nodo del que se desea calcular el coeficiente de clustering.

        Retorna:
        - float: Coeficiente de clustering del nodo.
        """
        vecinos = self.red.get(nodo, [])
        nv = 0
        for vecino, _ in vecinos:
            vecinos_dvecino = set(self.red.get(vecino, []))
            for pos_vecino, _ in vecinos_dvecino:
                if pos_vecino in set(v for v, _ in vecinos):
                    nv += 1
        kv = self.k(nodo)
        coef_clustering = 'None' if kv < 2 else ((2 * nv) / (kv * (kv - 1)))
        return coef_clustering

    def plot_ck(self):
        """
        Grafica el coeficiente de clustering en función de la conectividad de los nodos.
        """
        nodos = list(self.red.keys())
        grados = [self.k(nodo) for nodo in nodos if self.k(nodo) > 2]
        grados_unicos = sorted(set(grados))
        coef_clust_promedio = [np.mean([self.ck(nodo) for nodo in nodos if self.k(nodo) == grado]) for grado in grados_unicos]
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=[16, 6])
        axs[0].scatter(grados_unicos, coef_clust_promedio, color='r')
        axs[0].set_title('C(k) linear')
        axs[0].set_xlabel('k')
        axs[0].set_ylabel('Ck')
        axs[0].grid(True)
        axs[1].scatter(grados_unicos, coef_clust_promedio, color='b')
        axs[1].set_title('C(k) log')
        axs[1].set_xlabel('k')
        axs[1].set_ylabel('Ck')
        axs[1].grid(True)
        axs[1].set_xscale('log')
        axs[1].set_yscale('log')
        plt.tight_layout()
        plt.show()

    def plot_pk(self):
        """
        Grafica la distribución de probabilidad de conectividad de los nodos.
        """
        nodos = list(self.red.keys())
        grados = [self.k(nodo) for nodo in nodos]
        frecuencias = {k: grados.count(k) for k in set(grados)}
        keys = list(frecuencias.keys())
        values = [frecuencias[k] for k in keys]
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
        axs[0].scatter(keys, values, marker='o', color='g')
        axs[0].set_title('P(k) - Linear')
        axs[0].set_xlabel('Grado (k)')
        axs[0].set_ylabel('Frecuencia')
        axs[0].grid(True)
        axs[1].scatter(keys, values, color='purple')
        axs[1].set_title('P(k) - Log-log')
        axs[1].set_xlabel('k')
        axs[1].set_ylabel('Frecuencia (log)')
        axs[1].set_xscale('log')
        axs[1].set_yscale('log')
        axs[1].grid(True)
        plt.tight_layout()
        plt.show()
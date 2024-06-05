# Nombre del Proyecto

Fecha: 08/01/2024

**Participantes**:

- Mario Limón <email:mariolh@lcg.unam.mx>
- Román Zamora <email: angelzl@lcg.unam.mx>

## Descripción del Problema
Dada una lista de interacciones se busca construir una red y obtener el coeficiente de clustering y la probabilidad de conectividad de la misma


## Especificación de Requisitos

Requisitos funcionales
- Python 3.x
- Bibliotecas `matplotlib` y `numpy`

Requisitos no funcionales
- Lista de interacciones


## Análisis y Diseño

Se comenzó por armar la red en diccionarios con keys de nodos y values de vecinos, una vez construida esta, se crearon funciones para calcular y graficar los atributos de una red:

- Coeficiente de Clustering (Ck)
- Probabilidad de conectividad (Pk)

Para los cuales se usan el calculo (Parseadores incluidos) por nodo de:
- Conectividad (k)
- Coeficiente de clustering (ck)

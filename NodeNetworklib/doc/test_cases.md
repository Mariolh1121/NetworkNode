# Casos de prueba o escenarios
Este documento describe los casos de prueba para el script de Python desarrollado para analizar y visualizar una red de interacciones genéticas contenida en un archivo de texto desde la línea de comandos. Los casos de prueba están diseñados para cubrir las diferentes funcionalidades del script y abordar posibles errores que puedan surgir durante su ejecución.

El archivo de entrada permite proporcionar la ruta de un archivo con la lista de interacciones genéticas. El script calcula diversas métricas de la red y genera gráficos para visualizar la distribución de conectividad de los nodos.
    
### Caso de prueba 1: Comprobación de la impresión del gráfico P(k)
+ Descripción: Verificar la impresión de la gráfica de pk a partir del archivo de interacciones
+ Archivo de interacciones en la siguiente ruta relativa: NodeNetworklib\test\Example1.txt
+ Resultado esperado:
Impresión de la gráfica de p(k)
```
python .\plot_pk.py ..\test\Example1.txt
```
### Caso de prueba 2: Ruta del archivo no exístente 
+ Descripción: Verificar la salida cuando la ruta del archivo no exíste 
+ Archivo de interacciones en la siguiente ruta relativa: NodeNetworklib\test\Example4.txt
+ Resultado esperado: Impresión de mensaje: "Error, archivo no encontrado: "
```
python .\k.py ..\test\Example4.txt queso
```
### Caso de prueba 3: Cuando el nodo a buscar no esta presente en la red
+ Descripción: Verificar que un nodo no esta en la red
+ Archivo de interacciones en la siguiente ruta relativa: NodeNetworklib\test\Example2.txt
+ Resultado esperado: Impresión de mensaje: "El nodo '{nodo}' no existe en la red."
```
 python .\ck.py ..\test\Example2.txt queso
```

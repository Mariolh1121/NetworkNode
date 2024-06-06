# NodeNetworklib

## Uso
Este proyecto proporciona herramientas para:
- Cargar datos de una red desde un archivo.
- Calcular el grado de los nodos.
- Calcular el coeficiente de clustering de los nodos.
- Graficar el coeficiente de clustering promedio en función del grado de los nodos.
- Graficar la distribución de grados de la red.

El script está diseñado para operar en archivos de texto plano, con un número por línea. No hay restricciones en el número de líneas en el archivo.

## Descripción
Este paquete tiene como fin usar un archivo de texto plano de dos columnas, describiendo interacciones entre genes, formando una red, con esta información, este paquete calcula dos de los atributos más importantes de una red, el coeficiente de clustering y el potencial de conectividad

## Instalación
Este paquete se descarga y se utiliza desde la linea de comandos de python, usando el parseo de los argumentos

## Pruebas
### Módulo de ck:
python ck.py <path_del_archivo_de_interacciones> <nodo_del_que_se_requiere_el_ck>

### Módulo de k:
python k.py <path_del_archivo_de_interacciones> <nodo_del_que_se_requiera_la_conectividad>

### Módulo de plot_pk:
python plot_pk.py <path_del_archivo_de_interacciones>

### Módulo de plot_ck:
python plot_ck.py <path_del_archivo_de_interacciones>

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia MIT License. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [mariolh@lcg.unam.mx].

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [mariolh@lcg.unam.mx].

## Autores y Reconocimientos
- Mario Alberto Limón Hernandez
- Ángel Román Zamora López

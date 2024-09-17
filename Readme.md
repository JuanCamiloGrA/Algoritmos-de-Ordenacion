# Proyecto de Algoritmos de Ordenamiento

Este proyecto implementa y compara varios algoritmos de ordenamiento en Python. Los algoritmos incluidos son:

- Burbuja
- Inserción
- Selección
- MergeSort
- QuickSort

> El proyecto también se encuentra disponible en https://replit.com/@juangrisalesari/Algoritmos-de-ordenacion para su ejecución en línea.

## Estructura del Proyecto

- `main.py`: Archivo principal que ejecuta los algoritmos y guarda los resultados.
- `Algoritmos/`: Carpeta que contiene las implementaciones de los algoritmos de ordenamiento.
  - `burbuja.py`
  - `insercion.py`
  - `mergesort.py`
  - `quicksort.py`
  - `seleccion.py`
- `capturar_salida.py`: Módulo para guardar la lista ordenada en un archivo de texto.
- `leer_lista.py`: Módulo para leer las listas de entrada desde archivos.
- `generar_archivos.py`: Módulo para generar listas de entrada aleatorias.
- `RESULTADOS FINALES.txt`: Archivo con los resultados de las ejecuciones de los algoritmos.

## Integrantes

- Juan Camilo Grisales Arias
- Juan Felipe Tarazona Gonzales
- Kevin Andrés Betancourt López

## Requisitos

- Python >= 3.12
- PyCharm 2024.2.1 (opcional, pero recomendado para desarrollo)

## Ejecución

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio.
2. Asegúrate de tener las listas de entrada en el formato adecuado.
3. Ejecuta `main.py` para correr los algoritmos y guardar los resultados.

```bash
python main.py
```

## Resultados

Los resultados de las ejecuciones se imprimirán en la consola. Los resultados incluyen:

- Tiempo de ejecución
- Número de comparaciones
- Número de intercambios (si aplica)

## Ejemplo de Resultados

```plaintext
BURBUJA para 800 elementos:
  Tiempo de ejecución: 0.05793356895446777 segundos
  Comparaciones: 639200
  Intercambios: 161065
----------------------------------------
...
```

## Objetivos del Proyecto

El objetivo principal de este proyecto es implementar y comparar la eficiencia de varios algoritmos de ordenamiento en términos de tiempo de ejecución, número de comparaciones y número de intercambios.

## Metodología

Se implementaron cinco algoritmos de ordenamiento en Python. Cada algoritmo se ejecutó con listas de diferentes tamaños (800, 8000 y 80000 elementos) y se midieron los tiempos de ejecución, comparaciones e intercambios. En un principio, se usó un archivo `generar_archivos.py` para generar los archivos txt con las listas de diferentes tamaños.

## Conclusiones

A partir de los resultados obtenidos, se puede concluir que los algoritmos de ordenamiento más eficientes en términos de tiempo de ejecución son MergeSort y QuickSort, mientras que los algoritmos de Burbuja, Inserción y Selección son menos eficientes para listas grandes.

import time

from Algoritmos.burbuja import burbuja
from Algoritmos.insercion import insertion
from Algoritmos.mergesort import MergeSort
from Algoritmos.quicksort import quicksort
from Algoritmos.seleccion import seleccion
from capturar_salida import guardar_lista_en_txt
from leer_lista import leer_listas

lista_800, lista_8000, lista_80000 = map(tuple, leer_listas())


def ejecutar_y_guardar_resultados(algoritmo, nombre_algoritmo, lista, tamaño):
    inicio = time.time()
    try:
        lista_ordenada, comparaciones, intercambios = algoritmo(list(lista))
    except ValueError:
        lista_ordenada, comparaciones = algoritmo(list(lista))
        intercambios = "N/A"
    tiempo_ejecucion = time.time() - inicio
    guardar_lista_en_txt(lista_ordenada, f"salida_{nombre_algoritmo}_{tamaño}.txt")

    print(f"{nombre_algoritmo.upper()} para {tamaño} elementos:")
    print(f"  Tiempo de ejecución: {tiempo_ejecucion} segundos")
    print(f"  Comparaciones: {comparaciones}")
    print(f"  Intercambios: {intercambios}")
    print("-" * 40)

    return tiempo_ejecucion, comparaciones, intercambios


# ---------------------- BURBUJA ----------------------
ejecutar_y_guardar_resultados(burbuja, "burbuja", lista_800, 800)
ejecutar_y_guardar_resultados(burbuja, "burbuja", lista_8000, 8000)
ejecutar_y_guardar_resultados(burbuja, "burbuja", lista_80000, 80000)

# ---------------------- INSERCION ----------------------
ejecutar_y_guardar_resultados(insertion, "insercion", lista_800, 800)
ejecutar_y_guardar_resultados(insertion, "insercion", lista_8000, 8000)
ejecutar_y_guardar_resultados(insertion, "insercion", lista_80000, 80000)

# ---------------------- SELECCION ----------------------
ejecutar_y_guardar_resultados(seleccion, "seleccion", lista_800, 800)
ejecutar_y_guardar_resultados(seleccion, "seleccion", lista_8000, 8000)
ejecutar_y_guardar_resultados(seleccion, "seleccion", lista_80000, 80000)

# ---------------------- MERGESORT ----------------------
ejecutar_y_guardar_resultados(MergeSort, "mergesort", lista_800, 800)
ejecutar_y_guardar_resultados(MergeSort, "mergesort", lista_8000, 8000)
ejecutar_y_guardar_resultados(MergeSort, "mergesort", lista_80000, 80000)

# ---------------------- QUICKSORT ----------------------
ejecutar_y_guardar_resultados(quicksort, "quicksort", lista_800, 800)
ejecutar_y_guardar_resultados(quicksort, "quicksort", lista_8000, 8000)
ejecutar_y_guardar_resultados(quicksort, "quicksort", lista_80000, 80000)

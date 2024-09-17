def quicksort(lista: list) -> tuple:
    """
    Ordena una lista utilizando el algoritmo de ordenación QuickSort.

    Args:
        lista (list): La lista de elementos a ordenar.

    Returns:
        tuple: Una tupla que contiene la lista ordenada, el número de comparaciones y el número de intercambios.
    """
    comparisons = 0  # Contador de comparaciones
    swaps = 0  # Contador de intercambios

    # Caso base: si la lista tiene menos de 2 elementos, ya está ordenada
    if len(lista) < 2:
        return lista, comparisons, swaps

    pivote = lista[0]  # Elegir el primer elemento como pivote
    menores = []  # Lista para elementos menores que el pivote
    mayores = []  # Lista para elementos mayores o iguales al pivote

    # Particionar la lista en menores y mayores
    for i in range(1, len(lista)):
        comparisons += 1  # Incrementa comparaciones en cada comparación
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    # Ordenar recursivamente las sublistas
    menores_ordenados, comp_men, swaps_men = quicksort(menores)
    mayores_ordenados, comp_may, swaps_may = quicksort(mayores)
    comparisons += comp_men + comp_may  # Sumar comparaciones de las llamadas recursivas
    swaps += swaps_men + swaps_may  # Sumar intercambios de las llamadas recursivas

    # Combinar las listas ordenadas y el pivote
    lista_ordenada = menores_ordenados + [pivote] + mayores_ordenados

    return lista_ordenada, comparisons, swaps  # Retorna la lista ordenada, comparaciones e intercambios

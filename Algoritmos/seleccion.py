def seleccion(lista: list) -> list:
    """
    Ordena una lista utilizando el algoritmo de ordenación por selección.

    Args:
        lista (list): La lista de elementos a ordenar.

    Returns:
        tuple: Una tupla que contiene la lista ordenada, el número de comparaciones y el número de intercambios.
    """
    comparisons = 0  # Contador de comparaciones
    swaps = 0  # Contador de intercambios
    n = len(lista)

    # Iterar sobre cada elemento de la lista
    for i in range(n - 1):
        min_idx = i  # Índice del elemento mínimo

        # Encontrar el elemento mínimo en la sublista restante
        for j in range(i + 1, n):
            comparisons += 1  # Incrementa comparaciones en cada comparación
            if lista[j] < lista[min_idx]:
                min_idx = j

        # Intercambiar el elemento mínimo con el primer elemento de la sublista
        if min_idx < n and min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            swaps += 1  # Incrementa intercambios en cada intercambio

    return lista, comparisons, swaps  # Retorna la lista ordenada, comparaciones e intercambios

def insertion(lista: list) -> tuple:
    """
    Ordena una lista utilizando el algoritmo de ordenación por inserción.

    Args:
        lista (list): La lista de elementos a ordenar.

    Returns:
        tuple: Una tupla que contiene la lista ordenada, el número de comparaciones y el número de intercambios.
    """
    comparisons = 0  # Contador de comparaciones
    swaps = 0  # Contador de intercambios

    # Iterar sobre cada elemento de la lista comenzando desde el segundo
    for i in range(1, len(lista)):
        key = lista[i]  # Elemento a insertar en la posición correcta
        j = i - 1

        # Mover los elementos de la lista que son mayores que la clave un lugar hacia adelante
        while j >= 0 and key < lista[j]:
            comparisons += 1
            lista[j + 1] = lista[j]
            j -= 1
            swaps += 1

        # Insertar la clave en su posición correcta
        lista[j + 1] = key
        if j >= 0:
            comparisons += 1

    return lista, comparisons, swaps

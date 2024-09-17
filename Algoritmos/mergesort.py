def MergeSort(lista):
    """
        Ordena una lista utilizando el algoritmo de ordenación MergeSort.

        Args:
            lista (list): La lista de elementos a ordenar.

        Returns:
            tuple: Una tupla que contiene la lista ordenada y el número de comparaciones realizadas.
        """
    comparisons = 0
    if len(lista) <= 1:
        return lista, comparisons

    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Ordenar recursivamente cada mitad
    izquierda_ordenada, comp_izq = MergeSort(izquierda)
    derecha_ordenada, comp_der = MergeSort(derecha)
    comparisons += comp_izq + comp_der  # Sumar comparaciones de las llamadas recursivas

    # Combinar las dos listas ordenadas
    lista_ordenada, comp_mezcla = Mezclar(izquierda_ordenada, derecha_ordenada)
    comparisons += comp_mezcla

    return lista_ordenada, comparisons


def Mezclar(izquierda, derecha):
    """
        Mezcla dos listas ordenadas en una sola lista ordenada.

        Args:
            izquierda (list): La primera lista ordenada.
            derecha (list): La segunda lista ordenada.

        Returns:
            tuple: Una tupla que contiene la lista ordenada y el número de comparaciones realizadas.
        """
    lista_ordenada = []
    comparisons = 0

    # Mientras haya elementos en ambas listas
    while len(izquierda) > 0 and len(derecha) > 0:
        comparisons += 1  # Incrementa comparaciones en cada comparación del while
        if izquierda[0] < derecha[0]:
            lista_ordenada.append(izquierda[0])
            izquierda.pop(0)
        else:
            lista_ordenada.append(derecha[0])
            derecha.pop(0)

    # Si quedan elementos en alguna de las listas, los agregamos al final
    if len(izquierda) > 0:
        lista_ordenada += izquierda
    if len(derecha) > 0:
        lista_ordenada += derecha

    return lista_ordenada, comparisons

def MergeSort(lista):
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
    comparisons += comp_izq + comp_der #Sumar comparaciones de las llamadas recursivas

    # Combinar las dos listas ordenadas
    lista_ordenada, comp_mezcla = Mezclar(izquierda_ordenada, derecha_ordenada)
    comparisons += comp_mezcla

    return lista_ordenada, comparisons


def Mezclar(izquierda, derecha):
    lista_ordenada = []
    comparisons = 0

    # Mientras haya elementos en ambas listas
    while len(izquierda) > 0 and len(derecha) > 0:
        comparisons += 1 # Incrementa comparaciones en cada comparación del while
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

def quicksort(lista: list):
    comparisons = 0
    swaps = 0
    if len(lista) < 2:
        return lista, comparisons, swaps

    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):
        comparisons += 1  # Incrementa comparaciones en cada comparación
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    menores_ordenados, comp_men, swaps_men = quicksort(menores)
    mayores_ordenados, comp_may, swaps_may = quicksort(mayores)
    comparisons += comp_men + comp_may  #Sumar comparaciones de las llamadas recursivas
    swaps += swaps_men + swaps_may

    lista_ordenada = menores_ordenados + [pivote] + mayores_ordenados

    return lista_ordenada, comparisons, swaps  # Retorna la lista ordenada, comparaciones e intercambios

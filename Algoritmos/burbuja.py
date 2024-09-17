def burbuja(lista: list) -> tuple:
    # Inicializar contadores de comparaciones e intercambios
    comparisons = 0
    swaps = 0
    longitud = len(lista)

    # Bucle externo para cada elemento en la lista
    for i in range(longitud):
        # Bucle interno para comparar elementos adyacentes
        for j in range(longitud - i - 1):
            comparisons += 1
            # Intercambiar si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swaps += 1

    # Retornar la lista ordenada y los contadores
    return lista, comparisons, swaps

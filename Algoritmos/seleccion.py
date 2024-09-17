def seleccion(lista: list) -> list:
    comparisons = 0
    swaps = 0
    n = len(lista)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1  # Incrementa comparaciones en cada comparación
            if lista[j] < lista[min_idx]:
                min_idx = j

        if min_idx < n and min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            swaps += 1  # Incrementa intercambios en cada intercambio

    return lista, comparisons, swaps  # Retorna la lista ordenada, comparaciones e intercambios

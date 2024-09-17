def insertion(lista: list) -> list:
    comparisons = 0
    swaps = 0
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1

        while j >= 0 and key < lista[j]:
            comparisons += 1
            lista[j + 1] = lista[j]
            j -= 1
            swaps += 1

        lista[j + 1] = key
        if j >= 0:
            comparisons += 1

    return lista, comparisons, swaps

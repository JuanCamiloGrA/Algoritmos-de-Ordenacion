def burbuja(lista: list) -> list:
    comparisons = 0
    swaps = 0
    longitud = len(lista)

    for i in range(longitud):
        for j in range(longitud - i - 1):
            comparisons += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swaps += 1

    return lista, comparisons, swaps

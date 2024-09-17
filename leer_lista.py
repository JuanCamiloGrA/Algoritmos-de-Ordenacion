def leer_listas():
    archivos = ("Entrada-800.txt", "Entrada-8000.txt", "Entrada-80000.txt")

    for archivo in archivos:
        with open(archivo, "r") as f:
            contenido = f.read()
            lista = contenido.split(",")
            if archivo == "Entrada-800.txt":
                lista_800 = lista
            elif archivo == "Entrada-8000.txt":
                lista_8000 = lista
            else:
                lista_80000 = lista

    return lista_800, lista_8000, lista_80000

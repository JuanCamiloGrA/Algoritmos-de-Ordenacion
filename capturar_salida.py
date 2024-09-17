def guardar_lista_en_txt(lista, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(','.join(map(str, lista)))

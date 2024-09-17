import random

archivos = {
    "Entrada-800.txt": 800,
    "Entrada-8000.txt": 8000,
    "Entrada-80000.txt": 80000,
}


def generar_archivos(archivos):
    for archivo, cantidad in archivos.items():
        with open(archivo, "w") as f:
            numeros = (str(random.randint(1, 1000000)) for _ in range(cantidad))
            f.write(",".join(numeros))


generar_archivos(archivos)

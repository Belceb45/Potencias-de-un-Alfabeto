import time

def sigma_asterisco(alfabeto, n):
    # print("Σ* = {ε, ", end="")  # ε representa la cadena vacía
    contador = 1  # Contamos la cadena vacía

    for longitud in range(1, n + 1):
        total = len(alfabeto)
        combinaciones = total ** longitud

        for i in range(combinaciones):
            cadena = []
            temp = i

            for _ in range(longitud):
                cadena.insert(0, alfabeto[temp % total])
                temp //= total

            # print("".join(cadena), end=" ")
            contador += 1

    # print("... }")  # Indicar que la salida fue truncada
    return contador

# Entrada del usuario
alfabeto = input("Ingresa los símbolos del alfabeto separados por espacio: ").split()
n = int(input("Ingresa n: "))

# Medir tiempo de ejecución
inicio = time.time()
total_cadenas = sigma_asterisco(alfabeto, n)
fin = time.time()

# Mostrar cantidad total de cadenas generadas y tiempo de ejecución
print(f"Total de cadenas generadas: {total_cadenas}")
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

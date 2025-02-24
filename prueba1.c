#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void generarCadenas(char *buffer, char *alfabeto, int nivel, int n, int len_alfabeto, unsigned long long int *contador) {
    if (nivel > n) return;  // Límite de profundidad alcanzado

    (*contador)++;
    
    for (int i = 0; i < len_alfabeto; i++) {
        buffer[nivel] = alfabeto[i];
        buffer[nivel + 1] = '\0';
        generarCadenas(buffer, alfabeto, nivel + 1, n, len_alfabeto, contador);
    }
}

int main() {
    char alfabeto[50];  // Máximo 50 caracteres en el alfabeto
    int n;

    printf("Ingresa los simbolos del alfabeto sin espacios (ej. 01): ");
    scanf("%s", alfabeto);
    
    printf("Ingresa n: ");
    scanf("%d", &n);

    int len_alfabeto = strlen(alfabeto);

    if (n < 0) {
        printf("ERROR: SOLO NÚMEROS POSITIVOS\n");
        return 1;
    }

    // Medir tiempo de ejecución
    clock_t inicio = clock();

    char *buffer = (char *)malloc((n + 1) * sizeof(char));  // Buffer dinámico
    if (!buffer) {
        printf("ERROR: No se pudo asignar memoria.\n");
        return 1;
    }
    buffer[0] = '\0';

    unsigned long long int contador = 0;
    printf("\nE* = e, ");  // La cadena vacía (ε)
    generarCadenas(buffer, alfabeto, 0, n, len_alfabeto, &contador);
    
    clock_t fin = clock();

    free(buffer);  // Liberar memoria dinámica

    printf("\nTotal de cadenas generadas: %d\n", contador);
    printf("Tiempo de ejecucion: %.6f segundos\n", ((double)(fin - inicio)) / CLOCKS_PER_SEC);
    
    return 0;
}

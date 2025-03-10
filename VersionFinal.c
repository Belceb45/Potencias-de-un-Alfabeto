/*
    INSTITUTO POLITECNICO NACIONAL

            ESCOM

    Materia  --->   TEORIA COMPUTACIONAL
    Grupo    --->   4CM2
    Profesor --->   Genaro Juarez Martinez
    Alumno   --->   Rubio Haro Diego
*/

/*  Programa Universo (Primer programa)*/
/*
    //////////////////////////////////////////////////////////
    Programar el universo de las cadenas binarias (\Sigma^n).
    Dada una "n" que introduzca el usuario o que el programa
    lo determine automáticamente. El rango de "n" debe de estar
    en el intervalo de [0, 1000].
    //////////////////////////////////////////////////////////


*/

// Librerias
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Funcion que genera el universo de cadenas
void generarCombinacionesConComa(FILE *archivo, char *alfabeto, int len_alfabeto, int k, unsigned long long int *contador)
{
    /*
        Se hace un manejo de tipo de dato 'unsigned long long int' para evitar
        la falta de capacidad en el manejo de estos valores en el tipo de dato,
        teniendo como rango el siguiente: De 0 a 18,446,744,073,709,551,615 o
        2^64 - 1.
    */
    if (k == 0)
        return;

    unsigned long long int total = 1;
    for (int i = 0; i < k; i++)
    {
        total *= len_alfabeto;
    }

    char *buffer = (char *)malloc((k + 1) * sizeof(char));
    buffer[k] = '\0';

    for (unsigned long long int num = 0; num < total; num++)
    {
        unsigned long long int temp = num;
        for (int i = k - 1; i >= 0; i--)
        {
            buffer[i] = alfabeto[temp % len_alfabeto];
            temp /= len_alfabeto;
        }
        fprintf(archivo, ",%s", buffer);
        (*contador)++;
    }

    free(buffer);
}

// Funcion principal main
int main()
{
    int condition = 1;
    // Menu
    do
    {
        system("clear");
        printf("------------------>  Version Recursiva  <------------------\n");
        printf("-------                                             -------\n");
        printf("-------          ALFABETO (ej. 01 o ab):  ");

        char alfabeto[50];
        scanf("%s", alfabeto);

        int len_alfabeto = strlen(alfabeto);

        printf("-------\n");
        printf("-------                                               -------\n");

        printf("\n\n    1. Ingresar numero    2. Aleatorio 1-1000    3.Salir\n\n\t\t R: ");
        int opt;
        scanf("%d", &opt);

        if (opt == 1 || opt == 2)
        {
            // Apertura de archivo
            FILE *archivo = fopen("sigma_asterisco.txt", "w");
            if (!archivo)
            {
                printf("ERROR: No se pudo crear el archivo.\n");
                continue;
            }

            fprintf(archivo, "E* = { e");
            unsigned long long int contador = 1;

            int n = 0;
            printf("\n-------------------------------------------------------\n");
            if (opt == 1)
            {
                printf("\n  Ingresa n: ");
                scanf("%d", &n);
                if (n < 0)
                {
                    printf("ERROR: SOLO NÚMEROS POSITIVOS\n");
                    fclose(archivo);
                    continue;
                }
            }
            else if (opt == 2)
            {
                srand(time(NULL));
                n = 1 + rand() % 1000;
                printf("\n\nNumero aleatorio: %d ", n);
            }

            clock_t inicio = clock();
            for (int k = 1; k <= n; k++)
            {
                generarCombinacionesConComa(archivo, alfabeto, len_alfabeto, k, &contador);
            }
            clock_t final = clock();
            fprintf(archivo, " }");

            fclose(archivo);

            system("clear");
            printf("\nArchivo generado");
            printf("\nTotal de cadenas generadas: %llu\n", contador);
            printf("Tiempo de ejecucion: %.6f segundos\n", ((double)(final - inicio)) / CLOCKS_PER_SEC);

            char command[200];
            printf("\n\nGraficando............");
            // Precuacion: Para n>28 evitar graficar, pues python sufre de un error de memoria
            sprintf(command, "python graficaC.py sigma_asterisco.txt");
            system(command);
            printf("\n\nDeseas calcular de nuevo n (si o no)?: ");
            char opcion[15];
            scanf(" %s", &opcion);
            if (stricmp("no", opcion) == 0)
            {
                return 0;
            }

            else if (stricmp("si", opcion) == 0)
            {
            }
            else
            {
                printf("ERROR,PALABRA INVALIDA");
                return 0;
            }
        }
        else if (opt == 3)
        {
            printf("\n\nSaliendo del programa.......... \n\n");
            condition = 0;
        }
        else
        {
            printf("ERROR: SELECCIONA UNA OPCION VALIDA\n");
        }

    } while (condition);

    return 0;
}
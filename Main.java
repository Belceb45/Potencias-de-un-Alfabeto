/*
 *   INSTITUTO POLITECNICO NACIONAL 
 *  
 *     --->     ESCOM     <----
 *     --->     4CM2
 *   
 *    < TEORIA DE LA COMPUTACION >
 *      
 *    Profesor: Genaro Juarez Martinez
 *    Alumno:   Rubio Haro Diego
 * 
 * 
 *    Programa 1: Potencias de un Alfabeto / Sigma Asterisco (Iterativo)
 */
package Programa1;
 import java.util.Scanner;

 public class Main {
 
     public static void sigmaAsterisco(char[] alfabeto, int n) {
        //  System.out.print("Σ* = {ε, "); // ε representa la cadena vacía
         
         long contador = 1; // Contar la cadena vacía
         
         long inicio = System.nanoTime();
         
         for (int i = 1; i <= n; i++) {
             generarCadenas(alfabeto, i);
             contador += Math.pow(alfabeto.length, i);
         }
 
         long fin = System.nanoTime();
 
        //  System.out.println("... }");
         System.out.println("Total de cadenas generadas: " + contador);
         System.out.printf("Tiempo de ejecución: %.6f segundos\n", (fin - inicio) / 1e9);
     }
 
     public static void generarCadenas(char[] alfabeto, int longitud) {
         int total = alfabeto.length;
         int combinaciones = (int) Math.pow(total, longitud);
         
         for (int i = 0; i < combinaciones; i++) {
             StringBuilder cadena = new StringBuilder();
             int temp = i;
             
             for (int j = 0; j < longitud; j++) {
                 cadena.insert(0, alfabeto[temp % total]);
                 temp /= total;
             }
             
            //  System.out.print(cadena + " ");
         }
     }
 
     public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         System.out.println("PROGRAMA: POTENCIAS DE UN ALFABETO");
         
         System.out.print("Ingresa los símbolos del alfabeto separados por espacio: ");
         String[] inputAlfabeto = sc.nextLine().split(" ");
         char[] alfabeto = new char[inputAlfabeto.length];
 
         for (int i = 0; i < inputAlfabeto.length; i++) {
             alfabeto[i] = inputAlfabeto[i].charAt(0);
         }
 
         System.out.print("Ingresa n: ");
         int n = sc.nextInt();
 
         if (n < 0) {
             System.out.println("ERROR: SOLO NÚMEROS POSITIVOS");
         } else {
            //  System.out.println("\nAlfabeto: Σ = " + java.util.Arrays.toString(alfabeto));
             sigmaAsterisco(alfabeto, n);
         }
 
         sc.close();
     }
 }
 
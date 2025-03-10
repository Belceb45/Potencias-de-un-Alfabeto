import sys
import matplotlib.pyplot as plt
import multiprocessing

# Configuración de estilo
plt.style.use("dark_background")
COLOR_LINEAS = "#3E77B6"  # Azul
COLOR_FONDO = "#2C2C2C"   # Negro
COLOR_TEXTO = "#FFFFFF"    # Blanco

# Función para procesar cada bloque del archivo
def procesar_bloque(bloque):
    cadenas = []
    if "{" in bloque:
        bloque = bloque.split("{", 1)[1]
    if "}" in bloque:
        bloque = bloque.split("}")[0]
    
    cadenas = [cadena.strip() for cadena in bloque.split(",") if cadena.strip()]
    return cadenas

# Función para leer el archivo en paralelo
def leer_en_paralelo(archivo):
    cadenas_totales = []

    with open(archivo, "r") as f:
        # Leer el archivo en bloques de 1MB
        bloques = []
        while True:
            bloque = f.read(512*1024)  # Leer 512 KB a la vez  
            if not bloque:
                break
            bloques.append(bloque)

        # Usar múltiples procesos para procesar los bloques en paralelo
        with multiprocessing.Pool() as pool:
            # map() distribuirá los bloques a los procesos
            resultados = pool.map(procesar_bloque, bloques)

            # Aplanar la lista de resultados
            cadenas_totales.extend([cadena for resultado in resultados for cadena in resultado])

    return cadenas_totales

# Leer y procesar el archivo
if __name__ == "__main__":  # Esto es importante para evitar errores con multiprocessing en Windows
    if len(sys.argv) < 2:
        print("ERROR: Proporciona el archivo sigma_asterisco.txt")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        # Llamada para leer el archivo en paralelo
        cadenas = leer_en_paralelo(archivo)
    except FileNotFoundError:
        print(f"ERROR: Archivo {archivo} no encontrado.")
        sys.exit(1)

    # Calcular métricas por longitud
    longitud_maxima = max(len(cadena) for cadena in cadenas) if cadenas else 0

    acum_cadenas = []      
    acum_unos = []     
    acum_ceros = []      
    cadenas_por_longitud = []  
    unos_por_longitud = []     
    ceros_por_longitud = []    

    for long in range(1, longitud_maxima + 1):
        cadenas_long = [cadena for cadena in cadenas if len(cadena) == long]
        total_cadenas = len(cadenas_long)
        total_unos = sum(cadena.count("1") for cadena in cadenas_long)
        total_ceros = sum(cadena.count("0") for cadena in cadenas_long)
        
        cadenas_por_longitud.append(total_cadenas)
        unos_por_longitud.append(total_unos)
        ceros_por_longitud.append(total_ceros)
        
        acum_cadenas.append(sum(cadenas_por_longitud))
        acum_unos.append(sum(unos_por_longitud))
        acum_ceros.append(sum(ceros_por_longitud))

    # --- Imprimir estadísticas ---
    total_cadenas = sum(cadenas_por_longitud)
    total_unos = sum(unos_por_longitud)
    total_ceros = sum(ceros_por_longitud)

    print("\n--- ESTADÍSTICAS ---")
    print(f"Cadenas totales: {total_cadenas}")
    print(f"Total de '1's: {total_unos}")
    print(f"Total de '0's: {total_ceros}\n")

    # Configurar gráficas (como en tu código anterior)

    # Crear la figura y los subgráficos
    fig = plt.figure(figsize=(14, 10), facecolor=COLOR_FONDO)
    gs = fig.add_gridspec(2, 2)
    axs = [
        fig.add_subplot(gs[0, 0]),
        fig.add_subplot(gs[0, 1]),
        fig.add_subplot(gs[1, 0]),
        fig.add_subplot(gs[1, 1])
    ]

    # Estilo común para todas las gráficas
    for ax in axs:
        ax.set_facecolor(COLOR_FONDO)
        ax.tick_params(axis='both', colors=COLOR_TEXTO)
        ax.spines['bottom'].set_color(COLOR_TEXTO)
        ax.spines['left'].set_color(COLOR_TEXTO)
        ax.grid(True, alpha=0.2, color=COLOR_TEXTO)

    # --- Gráficas (como en tu código anterior) ---
    # --- Gráfica 1: Densidad de '1's por cadena (Optimizada) ---
    print(longitud_maxima)
    axs[0].plot(range(1, longitud_maxima + 1), acum_unos[:longitud_maxima], color=COLOR_LINEAS, marker="o", markersize=5, linewidth=2)
    axs[1].semilogy(range(1, longitud_maxima + 1), acum_unos[:longitud_maxima], color=COLOR_LINEAS, marker="s", linewidth=2)
    axs[2].plot(range(1, longitud_maxima + 1), acum_ceros[:longitud_maxima], color=COLOR_LINEAS, marker="o", markersize=5, linewidth=2)
    axs[3].semilogy(range(1, longitud_maxima + 1), acum_ceros[:longitud_maxima], color=COLOR_LINEAS, marker="D", linewidth=2)

    axs[0].set_title("Crecimiento de '1's en función de n", color=COLOR_TEXTO, fontsize=12, fontweight='bold', pad=15)
    axs[0].set_xlabel("Longitud de las cadenas (n)", color=COLOR_TEXTO)
    axs[0].set_ylabel("Densidad de '1s'", color=COLOR_TEXTO)

    # --- Gráfica 2: Cadenas acumuladas (Log) ---
    axs[1].set_title("Log10 densidad '1s'", color=COLOR_TEXTO, fontsize=12, fontweight='bold', pad=15)
    axs[1].set_xlabel("Longitud de las cadenas (n)", color=COLOR_TEXTO)
    axs[1].set_ylabel("Densidad de '1s'", color=COLOR_TEXTO)

    # --- Gráfica 3: '0's por longitud ---
    axs[2].set_title("Crecimiento de '0's en funcion de n", 
                    color=COLOR_TEXTO, 
                    fontsize=12,
                    fontweight='bold',
                    pad=15)
    axs[2].set_xlabel("Longitud de las cadenas (n)", color=COLOR_TEXTO)
    axs[2].set_ylabel("Densidad de '0s'", color=COLOR_TEXTO)

    # --- Gráfica 4: '0's acumulados (Log) ---
    axs[3].set_title("Log10 densidad '0s' ", 
                    color=COLOR_TEXTO, 
                    fontsize=12,
                    fontweight='bold',
                    pad=15)
    axs[3].set_xlabel("Longitud de las cadenas (n)", color=COLOR_TEXTO)
    axs[3].set_ylabel("Densidad de '0s'", color=COLOR_TEXTO)

    # Título principal
    fig.suptitle("ANÁLISIS DE CADENAS BINARIAS - TEORÍA COMPUTACIONAL 4CM2         RUBIO HARO DIEGO", 
                y=0.98,
                fontsize=16, 
                color=COLOR_TEXTO,
                fontweight="bold",
                backgroundcolor=COLOR_FONDO)

    # Añadir efecto de degradado al fondo
    fig.patch.set_facecolor(COLOR_FONDO)
    for ax in axs:
        ax.set_facecolor(COLOR_FONDO)
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, 
                    transform=ax.transAxes, 
                    zorder=-1,
                    alpha=0.3,
                    color=COLOR_LINEAS))

    plt.tight_layout(pad=3.0)
    plt.show()

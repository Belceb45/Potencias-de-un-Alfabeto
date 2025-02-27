import sys
import matplotlib.pyplot as plt
import math

# Configuración de estilo
plt.style.use("dark_background")
COLOR_LINEAS = "#3E77B6"  # Azul
COLOR_FONDO = "#2C2C2C"   # Negro
COLOR_TEXTO = "#FFFFFF"    # Blanco

# Leer y procesar el archivo
if len(sys.argv) < 2:
    print("ERROR: Proporciona el archivo sigma_asterisco.txt")
    sys.exit(1)

archivo = sys.argv[1]

try:
    with open(archivo, "r") as f:
        contenido = f.read().replace("E* = e, ", "").replace("e,", "").strip()
        cadenas = [cadena.strip() for cadena in contenido.split(",") if cadena.strip() and cadena.strip() != "e"]
except FileNotFoundError:
    print(f"ERROR: Archivo {archivo} no encontrado.")
    sys.exit(1)

# Calcular métricas por longitud
longitud_maxima = max(len(cadena) for cadena in cadenas) if cadenas else 0

acum_simbolos = []      
acum_unos = []           
simbolos_por_longitud = []  
unos_por_longitud = []      

for long in range(1, longitud_maxima + 1):
    cadenas_long = [cadena for cadena in cadenas if len(cadena) == long]
    total_simbolos = sum(len(cadena) for cadena in cadenas_long)
    total_unos = sum(cadena.count("1") for cadena in cadenas_long)
    print(total_simbolos)
    simbolos_por_longitud.append(total_simbolos)
    unos_por_longitud.append(total_unos)
    
    acum_simbolos.append(sum(simbolos_por_longitud))
    acum_unos.append(sum(unos_por_longitud))

# Configurar gráficas
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

# --- Gráfica 1: Símbolos por longitud ---
axs[0].plot(simbolos_por_longitud, 
           color=COLOR_LINEAS, 
           marker="o", 
           markersize=8,
           linewidth=2,
           markerfacecolor=COLOR_TEXTO)
axs[0].set_title("Grafica 1: Densidad de '1s'", 
                color=COLOR_TEXTO, 
                fontsize=12,
                fontweight='bold',
                pad=15)
axs[0].set_xlabel("Sigma 'n'", color=COLOR_TEXTO)
axs[0].set_ylabel("Numero de cadenas", color=COLOR_TEXTO)

# --- Gráfica 2: Símbolos Acumulados (Log) ---
axs[1].semilogy(acum_simbolos, 
               color=COLOR_LINEAS, 
               marker="s",
               linewidth=2)
axs[1].set_title("Logaritmo(e) de densidad '1s'", 
                color=COLOR_TEXTO, 
                fontsize=12,
                fontweight='bold',
                pad=15)
axs[1].set_xlabel("Sigma 'n'", color=COLOR_TEXTO)
axs[1].set_ylabel("Cantidad de cadenas", color=COLOR_TEXTO)
# --- Gráfica 3: '1's por longitud ---
axs[2].plot(unos_por_longitud, 
           color=COLOR_LINEAS, 
           marker="^",
           linewidth=2)
axs[2].set_title("Grafica 2: '1s' por cadena", 
                color=COLOR_TEXTO, 
                fontsize=12,
                fontweight='bold',
                pad=15)
axs[2].set_xlabel("Sigma 'n'", color=COLOR_TEXTO)
axs[2].set_ylabel("Numero de cadenas con '1'", color=COLOR_TEXTO)
# --- Gráfica 4: '1's Acumulados (Log) ---
axs[3].semilogy(acum_unos, 
               color=COLOR_LINEAS, 
               marker="D",
               linewidth=2)
axs[3].set_title("Logaritmo(e) de '1s' por cadena", 
                color=COLOR_TEXTO, 
                fontsize=12,
                fontweight='bold',
                pad=15)
axs[3].set_xlabel("Sigma 'n'", color=COLOR_TEXTO)
axs[3].set_ylabel("Numero de cadenas con '1'", color=COLOR_TEXTO)
# Título principal con estilo degradado
fig.suptitle("GRAFICAS SIGMA-ASTERISCO / TEORIA COMPUTACIONAL 4CM2         RUBIO HARO DIEGO", 
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
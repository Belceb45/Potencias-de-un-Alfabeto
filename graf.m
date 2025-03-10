% Configuración de estilo
COLOR_LINEAS = "#3E77B6";  % Azul
COLOR_FONDO = "#2C2C2C";   % Negro
COLOR_TEXTO = "#FFFFFF";   % Blanco

% Leer y procesar el archivo
if nargin < 1
    disp("ERROR: Proporciona el archivo sigma_asterisco.txt");
    return;
end

archivo = argv(){1};

try
    % Leer archivo
    contenido = fileread(archivo);
    
    % Limpiar encabezado y formato del archivo
    if contains(contenido, "{")
        contenido = strsplit(contenido, "{", 1){2};
    end
    if contains(contenido, "}")
        contenido = strsplit(contenido, "}", 1){1};
    end
    
    % Convertimos el contenido a una celda de cadenas
    cadenas = strsplit(strtrim(contenido), ",");
    cadenas = cadenas(~cellfun('isempty', cadenas));  % Eliminar cadenas vacías
catch
    disp(['ERROR: Archivo ', archivo, ' no encontrado.']);
    return;
end

% Calcular métricas por longitud
longitud_maxima = max(cellfun('length', cadenas));

acum_cadenas = zeros(1, longitud_maxima);
acum_unos = zeros(1, longitud_maxima);
acum_ceros = zeros(1, longitud_maxima);

% Contar las cadenas de acuerdo a la longitud
for long = 1:longitud_maxima
    % Seleccionar las cadenas de longitud 'long'
    cadenas_long = cadenas(cellfun('length', cadenas) == long);
    total_cadenas = length(cadenas_long);
    total_unos = sum(cellfun(@(x) sum(x == '1'), cadenas_long));
    total_ceros = sum(cellfun(@(x) sum(x == '0'), cadenas_long));
    
    acum_cadenas(long) = total_cadenas;
    acum_unos(long) = total_unos;
    acum_ceros(long) = total_ceros;
end

% --- Imprimir estadísticas ---
total_cadenas = sum(acum_cadenas);
total_unos = sum(acum_unos);
total_ceros = sum(acum_ceros);

disp("--- ESTADÍSTICAS ---");
disp(['Cadenas totales: ', num2str(total_cadenas)]);
disp(['Total de ''1''s: ', num2str(total_unos)]);
disp(['Total de ''0''s: ', num2str(total_ceros)]);

% Configuración para gráficas
figure('Color', COLOR_FONDO);
hold on;
set(gcf, 'Color', COLOR_FONDO);

% --- Gráfica 1: Densidad de '1's por cadena (Optimizada) ---
subplot(2, 2, 1);
plot(1:longitud_maxima, acum_unos(1:longitud_maxima), 'o-', 'LineWidth', 2, 'MarkerSize', 6, 'Color', COLOR_LINEAS);
title("Crecimiento de '1's en función de n", 'Color', COLOR_TEXTO);
xlabel("Longitud de las cadenas (n)", 'Color', COLOR_TEXTO);
ylabel("Cantidad acumulada de '1's", 'Color', COLOR_TEXTO);
set(gca, 'Color', COLOR_FONDO, 'XColor', COLOR_TEXTO, 'YColor', COLOR_TEXTO);

% --- Gráfica 2: Cadenas acumuladas (Log) ---
subplot(2, 2, 2);
semilogy(1:longitud_maxima, acum_cadenas(1:longitud_maxima), 's-', 'LineWidth', 2, 'Color', COLOR_LINEAS);
title("Log10 de Cadenas Acumuladas", 'Color', COLOR_TEXTO);
xlabel("Número de cadenas", 'Color', COLOR_TEXTO);
ylabel("Cadenas acumuladas (log10)", 'Color', COLOR_TEXTO);
set(gca, 'Color', COLOR_FONDO, 'XColor', COLOR_TEXTO, 'YColor', COLOR_TEXTO);

% --- Gráfica 3: '0's por longitud ---
subplot(2, 2, 3);
plot(1:longitud_maxima, acum_ceros(1:longitud_maxima), 'o-', 'LineWidth', 2, 'MarkerSize', 6, 'Color', COLOR_LINEAS);
title("'0's por longitud", 'Color', COLOR_TEXTO);
xlabel("Longitud (n)", 'Color', COLOR_TEXTO);
ylabel("Número de '0's", 'Color', COLOR_TEXTO);
set(gca, 'Color', COLOR_FONDO, 'XColor', COLOR_TEXTO, 'YColor', COLOR_TEXTO);

% --- Gráfica 4: '0's acumulados (Log) ---
subplot(2, 2, 4);
semilogy(1:longitud_maxima, acum_ceros(1:longitud_maxima), 'D-', 'LineWidth', 2, 'Color', COLOR_LINEAS);
title("Log10(Ceros)", 'Color', COLOR_TEXTO);
xlabel("Longitud (n)", 'Color', COLOR_TEXTO);
ylabel("'0's acumulados", 'Color', COLOR_TEXTO);
set(gca, 'Color', COLOR_FONDO, 'XColor', COLOR_TEXTO, 'YColor', COLOR_TEXTO);

% Título principal
suptitle("ANÁLISIS DE CADENAS BINARIAS - TEORÍA COMPUTACIONAL 4CM2         RUBIO HARO DIEGO", 'Color', COLOR_TEXTO);

hold off;

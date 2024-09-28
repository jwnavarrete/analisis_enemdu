import pandas as pd
import matplotlib.pyplot as plt
from filterData import filtrar_datos

# Esta función filtra los datos
FilterSueldoEmpleado = filtrar_datos()

# VARIABLES GLOBALES
Sexo = 'p02'
Sueldo = 'p66'
EstadoCivil = 'p06'
Experiencia = 'p45'
Etnia = 'p15'
NivelInstruccion = 'p10a'
PathPromedios = 'graficos/medidasEstadisticas/'

# Limpieza de datos: reemplazar espacios en blanco o cadenas vacías por NaN
FilterSueldoEmpleado[Experiencia] = FilterSueldoEmpleado[Experiencia].replace(' ', pd.NA)
FilterSueldoEmpleado[Sueldo] = FilterSueldoEmpleado[Sueldo].replace(' ', pd.NA)
FilterSueldoEmpleado[EstadoCivil] = FilterSueldoEmpleado[EstadoCivil].replace(' ', pd.NA)
FilterSueldoEmpleado[Etnia] = FilterSueldoEmpleado[Etnia].replace(' ', pd.NA)
FilterSueldoEmpleado[NivelInstruccion] = FilterSueldoEmpleado[NivelInstruccion].replace(' ', pd.NA)

# Eliminar filas con valores NaN en las columnas relevantes
FilterSueldoEmpleado = FilterSueldoEmpleado.dropna(subset=[Experiencia, Sueldo, EstadoCivil, Etnia, NivelInstruccion])

# Convertir las columnas a numérico, errores se manejan con 'coerce'
FilterSueldoEmpleado.loc[:, Experiencia] = pd.to_numeric(FilterSueldoEmpleado[Experiencia], errors='coerce')
FilterSueldoEmpleado.loc[:, Sueldo] = pd.to_numeric(FilterSueldoEmpleado[Sueldo], errors='coerce')
FilterSueldoEmpleado.loc[:, EstadoCivil] = pd.to_numeric(FilterSueldoEmpleado[EstadoCivil], errors='coerce')
FilterSueldoEmpleado.loc[:, Etnia] = pd.to_numeric(FilterSueldoEmpleado[Etnia], errors='coerce')
FilterSueldoEmpleado.loc[:, NivelInstruccion] = pd.to_numeric(FilterSueldoEmpleado[NivelInstruccion], errors='coerce')

# Calcular la matriz de correlación
print('************************************ Matriz de Correlación ********************************************')
correlation_matrix = FilterSueldoEmpleado.corr()
print(correlation_matrix)

# Calcular las medidas estadísticas
print('************************************ Medidas Estadísticas ********************************************')

print('************************************ Medias ********************************************')
print('Media de la Experiencia: ', FilterSueldoEmpleado[Experiencia].mean())
print('Media del Sueldo: ', FilterSueldoEmpleado[Sueldo].mean())
print('Media del Estado Civil: ', FilterSueldoEmpleado[EstadoCivil].mean())
print('Media de la Etnia: ', FilterSueldoEmpleado[Etnia].mean())
print('Media del Nivel de Instrucción: ', FilterSueldoEmpleado[NivelInstruccion].mean())

print('************************************ Medianas ********************************************')
print('Mediana de la Experiencia: ', FilterSueldoEmpleado[Experiencia].median())
print('Mediana del Sueldo: ', FilterSueldoEmpleado[Sueldo].median())
print('Mediana del Estado Civil: ', FilterSueldoEmpleado[EstadoCivil].median())
print('Mediana de la Etnia: ', FilterSueldoEmpleado[Etnia].median())
print('Mediana del Nivel de Instrucción: ', FilterSueldoEmpleado[NivelInstruccion].median())

print('************************************ Modas ********************************************')
print('Moda de la Experiencia: ', FilterSueldoEmpleado[Experiencia].mode()[0])
print('Moda del Sueldo: ', FilterSueldoEmpleado[Sueldo].mode()[0])
print('Moda del Estado Civil: ', FilterSueldoEmpleado[EstadoCivil].mode()[0])
print('Moda de la Etnia: ', FilterSueldoEmpleado[Etnia].mode()[0])
print('Moda del Nivel de Instrucción: ', FilterSueldoEmpleado[NivelInstruccion].mode()[0])

print('************************************ Desviaciones Estándar ********************************************')
print('Desviación Estándar de la Experiencia: ', FilterSueldoEmpleado[Experiencia].std())
print('Desviación Estándar del Sueldo: ', FilterSueldoEmpleado[Sueldo].std())
print('Desviación Estándar del Estado Civil: ', FilterSueldoEmpleado[EstadoCivil].std())
print('Desviación Estándar de la Etnia: ', FilterSueldoEmpleado[Etnia].std())

# Calcular el rango de las variables
print('************************************ Rangos ********************************************')
print('Rango de la Experiencia: ', FilterSueldoEmpleado[Experiencia].max() - FilterSueldoEmpleado[Experiencia].min())
print('Rango del Sueldo: ', FilterSueldoEmpleado[Sueldo].max() - FilterSueldoEmpleado[Sueldo].min())
print('Rango del Estado Civil: ', FilterSueldoEmpleado[EstadoCivil].max() - FilterSueldoEmpleado[EstadoCivil].min())
print('Rango de la Etnia: ', FilterSueldoEmpleado[Etnia].max() - FilterSueldoEmpleado[Etnia].min())
print('Rango del Nivel de Instrucción: ', FilterSueldoEmpleado[NivelInstruccion].max() - FilterSueldoEmpleado[NivelInstruccion].min())

# Calcular el curtosis de las variables
print('************************************ Curtosis ********************************************')
print('Curtosis de la Experiencia: ', FilterSueldoEmpleado[Experiencia].kurtosis())
print('Curtosis del Sueldo: ', FilterSueldoEmpleado[Sueldo].kurtosis())
print('Curtosis del Estado Civil: ', FilterSueldoEmpleado[EstadoCivil].kurtosis())
print('Curtosis de la Etnia: ', FilterSueldoEmpleado[Etnia].kurtosis())
print('Curtosis del Nivel de Instrucción: ', FilterSueldoEmpleado[NivelInstruccion].kurtosis())

# Calcular el cuartil de las variables
print('************************************ Cuartiles ********************************************')
cuartiles_experiencia = FilterSueldoEmpleado[Experiencia].quantile([0.25, 0.5, 0.75])
cuartiles_sueldo = FilterSueldoEmpleado[Sueldo].quantile([0.25, 0.5, 0.75])
cuartiles_estado_civil = FilterSueldoEmpleado[EstadoCivil].quantile([0.25, 0.5, 0.75])
cuartiles_etnia = FilterSueldoEmpleado[Etnia].quantile([0.25, 0.5, 0.75])
cuartiles_nivel_instruccion = FilterSueldoEmpleado[NivelInstruccion].quantile([0.25, 0.5, 0.75])

print(f'Cuartiles de la Experiencia:\n{cuartiles_experiencia}')
print(f'Cuartiles del Sueldo:\n{cuartiles_sueldo}')
print(f'Cuartiles del Estado Civil:\n{cuartiles_estado_civil}')
print(f'Cuartiles de la Etnia:\n{cuartiles_etnia}')
print(f'Cuartiles del Nivel de Instrucción:\n{cuartiles_nivel_instruccion}')

# Crear un gráfico de caja para los cuartiles de las variables
plt.figure(figsize=(10, 8))
data_to_plot = [FilterSueldoEmpleado[Experiencia], FilterSueldoEmpleado[Sueldo], FilterSueldoEmpleado[EstadoCivil], FilterSueldoEmpleado[Etnia], FilterSueldoEmpleado[NivelInstruccion]]
labels = ['Experiencia', 'Sueldo', 'Estado Civil', 'Etnia', 'Nivel de Instrucción']
box = plt.boxplot(data_to_plot, patch_artist=True, tick_labels=labels)

# Personalizar el gráfico
plt.xlabel('Variables')
plt.ylabel('Valores')
plt.title('Gráfico de Caja de los Cuartiles de las Variables')
plt.grid(True)

# Ajustar el tamaño de las etiquetas en el eje y para evitar solapamientos
plt.ylim(bottom=0)  # Ajustar el límite inferior del eje y si es necesario

# Ajustar el tamaño de las etiquetas en el eje x para evitar solapamientos
plt.xticks(rotation=45, ha='right')

plt.savefig(PathPromedios + 'cuartiles_box_plot.png')  # Guarda el gráfico como un archivo

# Calcular la asimetría de las variables
print('************************************ Asimetría ********************************************')
print('Asimetría de la Experiencia: ', FilterSueldoEmpleado[Experiencia].skew())
print('Asimetría del Sueldo: ', FilterSueldoEmpleado[Sueldo].skew())
print('Asimetría del Estado Civil: ', FilterSueldoEmpleado[EstadoCivil].skew())
print('Asimetría de la Etnia: ', FilterSueldoEmpleado[Etnia].skew())
print('Asimetría del Nivel de Instrucción: ', FilterSueldoEmpleado[NivelInstruccion].skew())


# Crear un gráfico de barras para las medidas estadísticas
labels = ['Experiencia', 'Sueldo', 'Estado Civil', 'Etnia', 'Nivel de Instrucción']
sizes = [FilterSueldoEmpleado[Experiencia].mean(), FilterSueldoEmpleado[Sueldo].mean(), FilterSueldoEmpleado[EstadoCivil].mean(), FilterSueldoEmpleado[Etnia].mean(), FilterSueldoEmpleado[NivelInstruccion].mean()]
colors = ['#66b3ff', '#ff9999', '#ffcc99', '#99ff99', '#ff6666']

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Variables')
plt.ylabel('Media')
plt.title('Medias de las Variables')
plt.savefig(PathPromedios + 'medias_bar_chart.png')  # Guarda el gráfico como un archivo

# Crear un gráfico de barras para las medidas estadísticas
sizes = [FilterSueldoEmpleado[Experiencia].median(), FilterSueldoEmpleado[Sueldo].median(), FilterSueldoEmpleado[EstadoCivil].median(), FilterSueldoEmpleado[Etnia].median(), FilterSueldoEmpleado[NivelInstruccion].median()]

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Variables')
plt.ylabel('Mediana')
plt.title('Medianas de las Variables')
plt.savefig(PathPromedios + 'medianas_bar_chart.png')  # Guarda el gráfico como un archivo

# Crear un gráfico de barras para las medidas estadísticas
sizes = [FilterSueldoEmpleado[Experiencia].mode()[0], FilterSueldoEmpleado[Sueldo].mode()[0], FilterSueldoEmpleado[EstadoCivil].mode()[0], FilterSueldoEmpleado[Etnia].mode()[0], FilterSueldoEmpleado[NivelInstruccion].mode()[0]]

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Variables')
plt.ylabel('Moda')
plt.title('Modas de las Variables')
plt.savefig(PathPromedios + 'modas_bar_chart.png')  # Guarda el gráfico como un archivo

# Crear un gráfico de barras para las medidas estadísticas
sizes = [FilterSueldoEmpleado[Experiencia].std(), FilterSueldoEmpleado[Sueldo].std(), FilterSueldoEmpleado[EstadoCivil].std(), FilterSueldoEmpleado[Etnia].std(), FilterSueldoEmpleado[NivelInstruccion].std()]

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Variables')
plt.ylabel('Desviación Estándar')
plt.title('Desviaciones Estándar de las Variables')
plt.savefig(PathPromedios + 'desviaciones_estandar_bar_chart.png')  # Guarda el gráfico como un archivo


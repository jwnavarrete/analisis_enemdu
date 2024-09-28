import pandas as pd
import matplotlib.pyplot as plt
from filterData import filtrar_datos

# This function filters the data
FilterSueldoEmpleado = filtrar_datos()

# VARIABLES GLOBALES
Sexo = 'p02'
Sueldo = 'p66'
EstadoCivil = 'p06'
Experiencia = 'p45'
Etnia = 'p15'
NivelInstruccion = 'p10a'  # Assuming 'p10' is the column for 'Nivel de instrucción'
PathPromedios = 'graficos/promediosSueldo/'

# 1. Sueldo Promedio de Hombres y Mujeres
# Calculate average salaries
totalHombres = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Sexo] == 1, Sueldo].mean()
totalMujeres = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Sexo] == 2, Sueldo].mean()

print(f'************************************ Sueldo Promedio de Hombres y Mujeres ********************************************')
print(f'Sueldo Promedio de Hombres: {totalHombres}')
print(f'Sueldo Promedio de Mujeres: {totalMujeres}')

# Create a bar chart for average salaries
labels = ['Hombres', 'Mujeres']
sizes = [totalHombres, totalMujeres]
colors = ['#66b3ff', '#ff9999']

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Sexo')
plt.ylabel('Sueldo Promedio')
plt.title('Sueldo Promedio de Hombres y Mujeres')
plt.savefig(f'{PathPromedios}sueldo_promedio_bar_chart.png')  # Save the chart


# 2. Sueldo Promedio por Experiencia (establecer rangos de experiencia)

# Calculate average salaries by experience
FilterSueldoEmpleado[Experiencia] = pd.to_numeric(FilterSueldoEmpleado[Experiencia], errors='coerce')
FilterSueldoEmpleado = FilterSueldoEmpleado.dropna(subset=[Experiencia])
FilterSueldoEmpleado[Experiencia] = FilterSueldoEmpleado[Experiencia].astype(int)
FilterSueldoEmpleado['Experiencia'] = pd.cut(FilterSueldoEmpleado[Experiencia], bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], labels=['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50'])

totalExperiencia = FilterSueldoEmpleado.groupby('Experiencia')[Sueldo].mean()

print(f'************************************ Sueldo Promedio por Experiencia ********************************************')
print(totalExperiencia)

# Create a bar chart for average salaries by experience
plt.figure(figsize=(12, 6))
totalExperiencia.plot(kind='bar', color='skyblue')
plt.xlabel('Experiencia')
plt.ylabel('Sueldo Promedio')
plt.title('Sueldo Promedio por Experiencia')
plt.savefig(f'{PathPromedios}sueldo_promedio_por_experiencia_bar_chart.png')  # Save the chart
# plt.show()

# 3. Sueldo Promedio por estado civil

# Calculate average salaries by marital status
totalCasados = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[EstadoCivil] == 1, Sueldo].mean()
totalSeparado = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[EstadoCivil] == 2, Sueldo].mean()
totalDivorciados = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[EstadoCivil] == 3, Sueldo].mean()
totalViudos = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[EstadoCivil] == 4, Sueldo].mean()
totalUnionLibre = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[EstadoCivil] == 5, Sueldo].mean()
totalSolteros = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[EstadoCivil] == 6, Sueldo].mean()

print(f'************************************ Sueldo Promedio por Estado Civil ********************************************')
print(f'Sueldo Promedio de Casados: {totalCasados}')
print(f'Sueldo Promedio de Separados: {totalSeparado}')
print(f'Sueldo Promedio de Divorciados: {totalDivorciados}')
print(f'Sueldo Promedio de Viudos: {totalViudos}')
print(f'Sueldo Promedio de Union Libre: {totalUnionLibre}')
print(f'Sueldo Promedio de Solteros: {totalSolteros}')

# Create a bar chart for average salaries by marital status
labels = ['Casados', 'Separados', 'Divorciados', 'Viudos', 'Union Libre', 'Solteros']
sizes = [totalCasados, totalSeparado, totalDivorciados, totalViudos, totalUnionLibre, totalSolteros]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

plt.figure(figsize=(10, 7))
plt.bar(labels, sizes, color=colors, edgecolor='black', alpha=0.7)
plt.xlabel('Estado Civil')
plt.ylabel('Sueldo Promedio')
plt.title('Sueldo Promedio por Estado Civil')
plt.savefig(f'{PathPromedios}sueldo_promedio_por_estado_civil_bar_chart.png')  # Save the chart

# 4. Sueldo Promedio por etnia
# Ensure 'Etnia' is numeric
FilterSueldoEmpleado[Etnia] = pd.to_numeric(FilterSueldoEmpleado[Etnia], errors='coerce')

# Calculate
totalIndigenas = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 1, Sueldo].mean()
totalAfroecuatorianos = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 2, Sueldo].mean()
totalNegros = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 3, Sueldo].mean()
totalMulatos = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 4, Sueldo].mean()
totalMontubios = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 5, Sueldo].mean()
totalMestizos = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 6, Sueldo].mean()
totalBlancos = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 7, Sueldo].mean()
totalOtros = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[Etnia] == 8, Sueldo].mean()

print(f'************************************ Sueldo Promedio por Etnia ********************************************')
print(f'Sueldo Promedio de Indigenas: {totalIndigenas}')
print(f'Sueldo Promedio de Afroecuatorianos: {totalAfroecuatorianos}')
print(f'Sueldo Promedio de Negros: {totalNegros}')
print(f'Sueldo Promedio de Mulatos: {totalMulatos}')
print(f'Sueldo Promedio de Montubios: {totalMontubios}')
print(f'Sueldo Promedio de Mestizos: {totalMestizos}')
print(f'Sueldo Promedio de Blancos: {totalBlancos}')
print(f'Sueldo Promedio de Otros: {totalOtros}')

# genera el grafico de suelo promedio por etnia
labels = ['Indígenas', 'Afroecuatorianos', 'Negros', 'Mulatos', 'Montubios', 'Mestizos', 'Blancos', 'Otros']
sizes = [totalIndigenas, totalAfroecuatorianos, totalNegros, totalMulatos, totalMontubios, totalMestizos, totalBlancos, totalOtros]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffccff', '#ffff99']

# Create bar chart
plt.figure(figsize=(10, 7))
plt.bar(labels, sizes, color=colors, edgecolor='black', alpha=0.7)
plt.xlabel('Etnia')
plt.ylabel('Sueldo Promedio')
plt.title('Sueldo Promedio por Etnia')
plt.xticks(rotation=15)
plt.savefig(f'{PathPromedios}sueldo_promedio_por_etnia_bar_chart.png')

# 5. Sueldo Promedio por Nivel de instrucción
# Ensure 'Nivel de instrucción' is numeric
FilterSueldoEmpleado[NivelInstruccion] = pd.to_numeric(FilterSueldoEmpleado[NivelInstruccion], errors='coerce')

# Calculate average salaries by level of education
totalNinguno = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 1, Sueldo].mean()
totalCentroAlfa = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 2, Sueldo].mean()
totalJardinInfa = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 3, Sueldo].mean()
totalJardinPrimaria = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 4, Sueldo].mean()
totalEduBasica = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 5, Sueldo].mean()
totalSecundaria = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 6, Sueldo].mean()
totalEducacionMedia = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 7, Sueldo].mean()
totalEducacionSuperiorNoUniv = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 8, Sueldo].mean()
totalEducacionSuperiorUniv = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 9, Sueldo].mean()
totalEducacionPostGrados = FilterSueldoEmpleado.loc[FilterSueldoEmpleado[NivelInstruccion] == 10, Sueldo].mean()

print(f'************************************ Sueldo Promedio por Nivel de Instrucción ********************************************')
print(f'Sueldo Promedio de Ninguno: {totalNinguno}')
print(f'Sueldo Promedio de Centro de Alfabetización: {totalCentroAlfa}')
print(f'Sueldo Promedio de Jardín de Infantes: {totalJardinInfa}')
print(f'Sueldo Promedio de Jardín de Primaria: {totalJardinPrimaria}')
print(f'Sueldo Promedio de Educación Básica: {totalEduBasica}')
print(f'Sueldo Promedio de Secundaria: {totalSecundaria}')
print(f'Sueldo Promedio de Educación Media: {totalEducacionMedia}')
print(f'Sueldo Promedio de Educación Superior No Universitaria: {totalEducacionSuperiorNoUniv}')
print(f'Sueldo Promedio de Educación Superior Universitaria: {totalEducacionSuperiorUniv}')
print(f'Sueldo Promedio de Educación de Postgrados: {totalEducacionPostGrados}')

# Create a bar chart for average salaries by level of education
labels = ['Ninguno', 'Centro de Alfabetización', 'Jardín de Infantes', 'Jardín de Primaria', 'Educación Básica', 'Secundaria', 'Educación Media', 'Educación Superior No Universitaria', 'Educación Superior Universitaria', 'Educación de Postgrados']
sizes = [totalNinguno, totalCentroAlfa, totalJardinInfa, totalJardinPrimaria, totalEduBasica, totalSecundaria, totalEducacionMedia, totalEducacionSuperiorNoUniv, totalEducacionSuperiorUniv, totalEducacionPostGrados]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffccff', '#ffcc66', '#c2f0c2', '#ff99cc']

plt.figure(figsize=(14, 8))
plt.bar(labels, sizes, color=colors, edgecolor='black', alpha=0.7)
plt.xlabel('Nivel de Instrucción')
plt.ylabel('Sueldo Promedio')
plt.title('Sueldo Promedio por Nivel de Instrucción')
plt.xticks(rotation=15)
plt.savefig(f'{PathPromedios}sueldo_promedio_por_nivel_instruccion_bar_chart.png')
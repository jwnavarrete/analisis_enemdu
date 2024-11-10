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
Bono = 'Bono'
NivelInstruccion = 'p10a'
PathPromedios = 'graficos/promedioBono/'

# 1. Promedio Bono por Hombre y Mujer
print(f'************************************ Promedio Bono por Hombre y Mujer ********************************************')
promedioBonoHombres = FilterSueldoEmpleado[FilterSueldoEmpleado[Sexo] == 1][Bono].mean()
promedioBonoMujeres = FilterSueldoEmpleado[FilterSueldoEmpleado[Sexo] == 2][Bono].mean()

print(f'Promedio Bono Hombres: {promedioBonoHombres}')
print(f'Promedio Bono Mujeres: {promedioBonoMujeres}')

# Create a bar chart for the average
labels = ['Hombres', 'Mujeres']
sizes = [promedioBonoHombres, promedioBonoMujeres]
colors = ['#66b3ff', '#ff9999']

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Sexo')
plt.ylabel('Promedio Bono')
plt.title('Promedio Bono por Hombres y Mujeres')
plt.savefig(f'{PathPromedios}promedio_bono_bar_chart.png')  # Save the graph as a file


# 2. Promedio Bono por Estado Civil
print(f'************************************ Promedio Bono por Estado Civil ********************************************')
# valida si la columna Bono tiene valores para poder calcular el promedio
promedioBonoCasados = FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 1][Bono].mean()
promedioBonoSeparados = FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 2][Bono].mean()
promedioBonoDivorciados = FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 3][Bono].mean()
promedioBonoViudos = FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 4][Bono].mean()
promedioBonoUnionLibre = FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 5][Bono].mean()
promedioBonoSolteros = FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 6][Bono].mean()

print(f'Promedio Bono Casados: {promedioBonoCasados}')
print(f'Promedio Bono Separados: {promedioBonoSeparados}')
print(f'Promedio Bono Divorciados: {promedioBonoDivorciados}')
print(f'Promedio Bono Viudos: {promedioBonoViudos}')
print(f'Promedio Bono Unión Libre: {promedioBonoUnionLibre}')
print(f'Promedio Bono Solteros: {promedioBonoSolteros}')

# Create a bar chart for the average
labels = ['Casados', 'Separados', 'Divorciados', 'Viudos', 'Unión Libre', 'Solteros']
sizes = [promedioBonoCasados, promedioBonoSeparados, promedioBonoDivorciados, promedioBonoViudos, promedioBonoUnionLibre, promedioBonoSolteros]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

plt.figure(figsize=(10, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Estado Civil')
plt.ylabel('Promedio Bono')
plt.title('Promedio Bono por Estado Civil')
plt.savefig(f'{PathPromedios}promedio_bono_estado_civil_bar_chart.png')  # Save the graph as a file


# 3. Promedio Bono por Etnia
print(f'************************************ Promedio Bono por Etnia ********************************************')
# valida si la columna Bono tiene valores para poder calcular el promedio
promedioBonoIndigena = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 1][Bono].mean()
promedioBonoAfroecuatoriano = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 2][Bono].mean()
promedioBonoNegro = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 3][Bono].mean()
promedioBonoMulato = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 4][Bono].mean()
promedioBonoMontubio = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 5][Bono].mean()
promedioBonoMestizo = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 6][Bono].mean()
promedioBonoBlanco = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 7][Bono].mean()
promedioBonoOtro = FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 8][Bono].mean()

print(f'Promedio Bono Indígena: {promedioBonoIndigena}')
print(f'Promedio Bono Afroecuatoriano: {promedioBonoAfroecuatoriano}')
print(f'Promedio Bono Negro: {promedioBonoNegro}')
print(f'Promedio Bono Mulato: {promedioBonoMulato}')
print(f'Promedio Bono Montubio: {promedioBonoMontubio}')
print(f'Promedio Bono Mestizo: {promedioBonoMestizo}')
print(f'Promedio Bono Blanco: {promedioBonoBlanco}')
print(f'Promedio Bono Otro: {promedioBonoOtro}')

# Create a bar chart for the average
labels = ['Indígena', 'Afroecuatoriano', 'Negro', 'Mulato', 'Montubio', 'Mestizo', 'Blanco', 'Otro']
sizes = [promedioBonoIndigena, promedioBonoAfroecuatoriano, promedioBonoNegro, promedioBonoMulato, promedioBonoMontubio,
          promedioBonoMestizo, promedioBonoBlanco, promedioBonoOtro]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4']

plt.figure(figsize=(12, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Etnia')
plt.ylabel('Promedio Bono')
plt.title('Promedio Bono por Etnia')
plt.savefig(f'{PathPromedios}promedio_bono_etnia_bar_chart.png')  # Save the graph as a file


# 4. Promedio Bono por Experiencia
print(f'************************************ Promedio Bono por Experiencia ********************************************')
# Define experience ranges
experience_ranges = {
    '0-1 años': (0, 1),
    '2-5 años': (2, 5),
    '6-10 años': (6, 10),
    '11-20 años': (11, 20),
    '21+ años': (21, float('inf'))
}

# Calculate average bonus for each experience range
promedios_bono_experiencia = {}
for label, (min_exp, max_exp) in experience_ranges.items():
    promedio = FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= min_exp) & (FilterSueldoEmpleado[Experiencia] <= max_exp)][Bono].mean()
    promedios_bono_experiencia[label] = promedio
    print(f'Promedio Bono {label}: {promedio}')

# Create a bar chart for the average
labels = list(promedios_bono_experiencia.keys())
sizes = list(promedios_bono_experiencia.values())
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(12, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Experiencia')
plt.ylabel('Promedio Bono')
plt.title('Promedio Bono por Experiencia')
plt.savefig(f'{PathPromedios}promedio_bono_experiencia_bar_chart.png')  # Save the graph as a file

# 5. Promedio Bono por Nivel de instrucción
print(f'************************************ Promedio Bono por Nivel de instrucción ********************************************')
# valida si la columna Bono tiene valores para poder calcular el promedio
promedioBonoNinguno = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 1][Bono].mean()
promedioBonoCentroAlfa = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 2][Bono].mean()
promedioBonoJardinInfa = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 3][Bono].mean()
promedioBonoJardinPrimaria = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 4][Bono].mean()
promedioBonoEduBasica = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 5][Bono].mean()
promedioBonoSecundaria = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 6][Bono].mean()
promedioBonoEducacionMedia = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 7][Bono].mean()
promedioBonoEducacionSuperiorNoUniv = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 8][Bono].mean()
promedioBonoEducacionSuperiorUniv = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 9][Bono].mean()
promedioBonoEducacionPostGrados = FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 10][Bono].mean()

print(f'Promedio Bono Ninguno: {promedioBonoNinguno}')
print(f'Promedio Bono Centro de Alfabetización: {promedioBonoCentroAlfa}')
print(f'Promedio Bono Jardín de Infantes: {promedioBonoJardinInfa}')
print(f'Promedio Bono Jardín y Primaria: {promedioBonoJardinPrimaria}')
print(f'Promedio Bono Educación Básica: {promedioBonoEduBasica}')
print(f'Promedio Bono Secundaria: {promedioBonoSecundaria}')
print(f'Promedio Bono Educación Media: {promedioBonoEducacionMedia}')
print(f'Promedio Bono Educación Superior No Universitaria: {promedioBonoEducacionSuperiorNoUniv}')
print(f'Promedio Bono Educación Superior Universitaria: {promedioBonoEducacionSuperiorUniv}')
print(f'Promedio Bono Educación de Postgrados: {promedioBonoEducacionPostGrados}')

# Create a bar chart for the average
labels = ['Ninguno', 'Alfabetización', 'Infantes', 'Primaria', 'Básica', 'Secundaria', 'Media', 'Sup. No Univ', 'Sup. Univ', 'Postgrados']
sizes = [promedioBonoNinguno, promedioBonoCentroAlfa, promedioBonoJardinInfa, promedioBonoJardinPrimaria, promedioBonoEduBasica,
          promedioBonoSecundaria, promedioBonoEducacionMedia, promedioBonoEducacionSuperiorNoUniv, promedioBonoEducacionSuperiorUniv, promedioBonoEducacionPostGrados]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#ffb347', '#ff6961']

plt.figure(figsize=(12, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Nivel de instrucción')
plt.ylabel('Promedio Bono')
plt.title('Promedio Bono por Nivel de instrucción')
plt.savefig(f'{PathPromedios}promedio_bono_nivel_instruccion_bar_chart.png')  # Save the graph as a file

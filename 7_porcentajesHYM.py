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
PathPromedios = 'graficos/porcentajesHYM/'


totalHombres = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Sexo] == 1])
totalMujeres = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Sexo] == 2])

# TOTALES DE ETNIA
totalIndigena = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 1])
totalAfro = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 2])
totalNegro = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 3])
totalMulato = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 4])
totalMontubio = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 5])
totalMestizo = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 6])
totalBlanco = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 7])
totalOtro = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 8])

# TOTALES DE ESTADO CIVIL
totalCasado = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 1])
totalSeparado = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 2])
totalDivorciado = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 3])
totalViudo = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 4])
totalUnionLibre = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 5])
totalSoltero = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 6])

# TOTALES DE EXPERIENCIA
totalSinExperiencia = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Experiencia] == 0])
totalMenosAnio = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Experiencia] == 1])
total1a3 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 2) & (FilterSueldoEmpleado[Experiencia] <= 3)])
total4a6 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 4) & (FilterSueldoEmpleado[Experiencia] <= 6)])
total7a9 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 7) & (FilterSueldoEmpleado[Experiencia] <= 9)])
total10a12 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 10) & (FilterSueldoEmpleado[Experiencia] <= 12)])
total13a15 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 13) & (FilterSueldoEmpleado[Experiencia] <= 15)])
total16a18 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 16) & (FilterSueldoEmpleado[Experiencia] <= 18)])
total19a21 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 19) & (FilterSueldoEmpleado[Experiencia] <= 21)])
total22a24 = len(FilterSueldoEmpleado[(FilterSueldoEmpleado[Experiencia] >= 22) & (FilterSueldoEmpleado[Experiencia] <= 24)])

# TOTALES DE NIVEL DE INSTRUCCIÓN
totalNinguno = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 1])
totalCentroAlfa = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 2])
totalJardinInfa = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 3])
totalJardinPrimaria = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 4])
totalEduBasica = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 5])
totalSecundaria = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 6])
totalEducacionMedia = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 7])
totalEducacionSuperiorNoUniv = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 8])
totalEducacionSuperiorUniv = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 9])
totalEducacionPostGrados = len(FilterSueldoEmpleado[FilterSueldoEmpleado[NivelInstruccion] == 10])



# HOMBRES **************************************************************

# 1. Hombres % por Etnia
print(f'************************************ Porcentaje de Hombres por Etnia ********************************************')

porcentajeIndigena = (totalIndigena / totalHombres) * 100
porcentajeAfro = (totalAfro / totalHombres) * 100
porcentajeNegro = (totalNegro / totalHombres) * 100
porcentajeMulato = (totalMulato / totalHombres) * 100
porcentajeMontubio = (totalMontubio / totalHombres) * 100
porcentajeMestizo = (totalMestizo / totalHombres) * 100
porcentajeBlanco = (totalBlanco / totalHombres) * 100
porcentajeOtro = (totalOtro / totalHombres) * 100

print(f'Porcentaje de Indigenas: {porcentajeIndigena}')
print(f'Porcentaje de Afro: {porcentajeAfro}')
print(f'Porcentaje de Negro: {porcentajeNegro}')
print(f'Porcentaje de Mulato: {porcentajeMulato}')
print(f'Porcentaje de Montubio: {porcentajeMontubio}')
print(f'Porcentaje de Mestizo: {porcentajeMestizo}')
print(f'Porcentaje de Blanco: {porcentajeBlanco}')
print(f'Porcentaje de Otro: {porcentajeOtro}')

# Create a bar chart for average salaries
labels = ['Indigena', 'Afro', 'Negro', 'Mulato', 'Montubio', 'Mestizo', 'Blanco', 'Otro']
sizes = [porcentajeIndigena, porcentajeAfro, porcentajeNegro, porcentajeMulato, porcentajeMontubio, porcentajeMestizo, porcentajeBlanco, porcentajeOtro]
colors = ['#66b3ff', '#ff9999', '#ffcc99', '#99ff99', '#66ff66', '#ff6666', '#ffcc66', '#c2c2f0']

plt.figure(figsize=(10, 7))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Etnia')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Hombres por Etnia')
plt.savefig(f'{PathPromedios}hombres_por_etnia_bar_chart.png')  # Save the chart


# 2. Hombres % por Estado Civil
print(f'************************************ Porcentaje de Hombres por Estado Civil ********************************************')
porcentajeCasado = (totalCasado / totalHombres) * 100
porcentajeSeparado = (totalSeparado / totalHombres) * 100
porcentajeDivorciado = (totalDivorciado / totalHombres) * 100
porcentajeViudo = (totalViudo / totalHombres) * 100
porcentajeUnionLibre = (totalUnionLibre / totalHombres) * 100
porcentajeSoltero = (totalSoltero / totalHombres) * 100

print(f'Porcentaje de Casados: {porcentajeCasado}')
print(f'Porcentaje de Separados: {porcentajeSeparado}')
print(f'Porcentaje de Divorciados: {porcentajeDivorciado}')
print(f'Porcentaje de Viudos: {porcentajeViudo}')
print(f'Porcentaje de Unión Libre: {porcentajeUnionLibre}')
print(f'Porcentaje de Solteros: {porcentajeSoltero}')

# Create a bar chart for percentage of men by marital status
labels_estado_civil = ['Casado', 'Separado', 'Divorciado', 'Viudo', 'Unión Libre', 'Soltero']
sizes_estado_civil = [porcentajeCasado, porcentajeSeparado, porcentajeDivorciado, porcentajeViudo, porcentajeUnionLibre, porcentajeSoltero]
colors_estado_civil = ['#66b3ff', '#ff9999', '#ffcc99', '#99ff99', '#66ff66', '#ff6666']

plt.figure(figsize=(10, 7))
plt.bar(labels_estado_civil, sizes_estado_civil, color=colors_estado_civil)
plt.xlabel('Estado Civil')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Hombres por Estado Civil')
plt.savefig(f'{PathPromedios}hombres_por_estado_civil_bar_chart.png')  # Save the chart

# 3. Hombres % por Experiencia
print(f'************************************ Porcentaje de Hombres por Experiencia ********************************************')
# Asegúrate de que la columna de experiencia sea numérica
FilterSueldoEmpleado[Experiencia] = pd.to_numeric(FilterSueldoEmpleado[Experiencia], errors='coerce')

# Suponiendo que totalHombres se definió previamente
porcentajeSinExperiencia = (totalSinExperiencia / totalHombres) * 100
porcentajeMenosAnio = (totalMenosAnio / totalHombres) * 100
porcentaje1a3 = (total1a3 / totalHombres) * 100
porcentaje4a6 = (total4a6 / totalHombres) * 100
porcentaje7a9 = (total7a9 / totalHombres) * 100
porcentaje10a12 = (total10a12 / totalHombres) * 100
porcentaje13a15 = (total13a15 / totalHombres) * 100
porcentaje16a18 = (total16a18 / totalHombres) * 100
porcentaje19a21 = (total19a21 / totalHombres) * 100
porcentaje22a24 = (total22a24 / totalHombres) * 100

# Imprimir resultados
print(f'Porcentaje de Sin Experiencia: {porcentajeSinExperiencia:.2f}%')
print(f'Porcentaje de Menos de un año: {porcentajeMenosAnio:.2f}%')
print(f'Porcentaje de 1 a 3 años: {porcentaje1a3:.2f}%')
print(f'Porcentaje de 4 a 6 años: {porcentaje4a6:.2f}%')
print(f'Porcentaje de 7 a 9 años: {porcentaje7a9:.2f}%')
print(f'Porcentaje de 10 a 12 años: {porcentaje10a12:.2f}%')
print(f'Porcentaje de 13 a 15 años: {porcentaje13a15:.2f}%')
print(f'Porcentaje de 16 a 18 años: {porcentaje16a18:.2f}%')
print(f'Porcentaje de 19 a 21 años: {porcentaje19a21:.2f}%')
print(f'Porcentaje de 22 a 24 años: {porcentaje22a24:.2f}%')

# Crear gráfico de barras para el porcentaje
labels_experiencia = ['Sin Experiencia', 'Menos de un año', '1 a 3 años', '4 a 6 años', '7 a 9 años', 
                      '10 a 12 años', '13 a 15 años', '16 a 18 años', '19 a 21 años', '22 a 24 años']
sizes_experiencia = [porcentajeSinExperiencia, porcentajeMenosAnio, porcentaje1a3, 
                     porcentaje4a6, porcentaje7a9, porcentaje10a12, 
                     porcentaje13a15, porcentaje16a18, porcentaje19a21, porcentaje22a24]

colors_experiencia = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', 
                      '#ffb3e6', '#c2f0c2', '#ff9999', '#ffcc99', '#66ff66']

plt.figure(figsize=(10, 7))
plt.bar(labels_experiencia, sizes_experiencia, color=colors_experiencia)
plt.xlabel('Experiencia')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Hombres por Experiencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{PathPromedios}hombres_por_experiencia_bar_chart.png')  # Save the chart
# plt.show()


# 4. Hombres % por Nivel de Instrucción
print(f'************************************ Porcentaje de Hombres por Nivel de Instrucción ********************************************')
porcentajeNinguno = (totalNinguno / totalHombres) * 100
porcentajeCentroAlfa = (totalCentroAlfa / totalHombres) * 100
porcentajeJardinInfa = (totalJardinInfa / totalHombres) * 100
porcentajeJardinPrimaria = (totalJardinPrimaria / totalHombres) * 100
porcentajeEduBasica = (totalEduBasica / totalHombres) * 100
porcentajeSecundaria = (totalSecundaria / totalHombres) * 100
porcentajeEducacionMedia = (totalEducacionMedia / totalHombres) * 100
porcentajeEducacionSuperiorNoUniv = (totalEducacionSuperiorNoUniv / totalHombres) * 100
porcentajeEducacionSuperiorUniv = (totalEducacionSuperiorUniv / totalHombres) * 100
porcentajeEducacionPostGrados = (totalEducacionPostGrados / totalHombres) * 100

print(f'Porcentaje de Ninguno: {porcentajeNinguno}')
print(f'Porcentaje de Centro de Alfabetización: {porcentajeCentroAlfa}')
print(f'Porcentaje de Jardín de Infantes: {porcentajeJardinInfa}')
print(f'Porcentaje de Jardín de Primaria: {porcentajeJardinPrimaria}')
print(f'Porcentaje de Educación Básica: {porcentajeEduBasica}')
print(f'Porcentaje de Secundaria: {porcentajeSecundaria}')
print(f'Porcentaje de Educación Media: {porcentajeEducacionMedia}')
print(f'Porcentaje de Educación Superior No Universitaria: {porcentajeEducacionSuperiorNoUniv}')
print(f'Porcentaje de Educación Superior Universitaria: {porcentajeEducacionSuperiorUniv}')
print(f'Porcentaje de Educación de Postgrados: {porcentajeEducacionPostGrados}')

# Create a bar chart for percentage
labels_instruccion = ['Ninguno', 'Centro Alfa', 'Jardín Inf.', 'Jardín Prim.', 'Edu. Básica', 
                      'Secundaria', 'Edu. Media', 'Sup. No Univ.', 'Sup. Univ.', 'Postgrados']
sizes_instruccion = [porcentajeNinguno, porcentajeCentroAlfa, porcentajeJardinInfa, porcentajeJardinPrimaria, porcentajeEduBasica, 
                     porcentajeSecundaria, porcentajeEducacionMedia, porcentajeEducacionSuperiorNoUniv, porcentajeEducacionSuperiorUniv, porcentajeEducacionPostGrados]
colors_instruccion = ['#66b3ff', '#ff9999', '#ffcc99', '#99ff99', '#66ff66', '#ff6666', '#ffcc66', '#c2c2f0', '#ffb3e6', '#c2f0c2']

plt.figure(figsize=(10, 7))
plt.bar(labels_instruccion, sizes_instruccion, color=colors_instruccion)
plt.xlabel('Nivel de Instrucción')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Hombres por Nivel de Instrucción')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{PathPromedios}hombres_por_nivel_instruccion_bar_chart.png')




# MUJERES **************************************************************

# 1. Mujeres % por Etnia
print(f'************************************ Porcentaje de Hombres por Etnia ********************************************')
porcentajeIndigena = (totalIndigena / totalMujeres) * 100
porcentajeAfro = (totalAfro / totalMujeres) * 100
porcentajeNegro = (totalNegro / totalMujeres) * 100
porcentajeMulato = (totalMulato / totalMujeres) * 100
porcentajeMontubio = (totalMontubio / totalMujeres) * 100
porcentajeMestizo = (totalMestizo / totalMujeres) * 100
porcentajeBlanco = (totalBlanco / totalMujeres) * 100
porcentajeOtro = (totalOtro / totalMujeres) * 100

print(f'Porcentaje de Indigenas: {porcentajeIndigena}')
print(f'Porcentaje de Afro: {porcentajeAfro}')
print(f'Porcentaje de Negro: {porcentajeNegro}')
print(f'Porcentaje de Mulato: {porcentajeMulato}')
print(f'Porcentaje de Montubio: {porcentajeMontubio}')
print(f'Porcentaje de Mestizo: {porcentajeMestizo}')
print(f'Porcentaje de Blanco: {porcentajeBlanco}')
print(f'Porcentaje de Otro: {porcentajeOtro}')

# Create a bar chart for average salaries
labels = ['Indigena', 'Afro', 'Negro', 'Mulato', 'Montubio', 'Mestizo', 'Blanco', 'Otro']
sizes = [porcentajeIndigena, porcentajeAfro, porcentajeNegro, porcentajeMulato, porcentajeMontubio, porcentajeMestizo, porcentajeBlanco, porcentajeOtro]
colors = ['#66b3ff', '#ff9999', '#ffcc99', '#99ff99', '#66ff66', '#ff6666', '#ffcc66', '#c2c2f0']

plt.figure(figsize=(10, 7))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Etnia')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Mujeres por Etnia')
plt.savefig(f'{PathPromedios}mujeres_por_etnia_bar_chart.png')  # Save the chart


# 2. Mujeres % por Estado Civil
print(f'************************************ Porcentaje de Mujeres por Estado Civil ********************************************')
porcentajeCasado = (totalCasado / totalMujeres) * 100
porcentajeSeparado = (totalSeparado / totalMujeres) * 100
porcentajeDivorciado = (totalDivorciado / totalMujeres) * 100
porcentajeViudo = (totalViudo / totalMujeres) * 100
porcentajeUnionLibre = (totalUnionLibre / totalMujeres) * 100
porcentajeSoltero = (totalSoltero / totalMujeres) * 100

print(f'Porcentaje de Casadas: {porcentajeCasado}')
print(f'Porcentaje de Separadas: {porcentajeSeparado}')
print(f'Porcentaje de Divorciadas: {porcentajeDivorciado}')
print(f'Porcentaje de Viudas: {porcentajeViudo}')
print(f'Porcentaje de Unión Libre: {porcentajeUnionLibre}')
print(f'Porcentaje de Solteras: {porcentajeSoltero}')

# Create a bar chart for percentage of women by marital status
labels_estado_civil = ['Casada', 'Separada', 'Divorciada', 'Viuda', 'Unión Libre', 'Soltera']
sizes_estado_civil = [porcentajeCasado, porcentajeSeparado, porcentajeDivorciado, porcentajeViudo, porcentajeUnionLibre, porcentajeSoltero]
colors_estado_civil = ['#66b3ff', '#ff9999', '#ffcc99', '#99ff99', '#66ff66', '#ff6666']

plt.figure(figsize=(10, 7))
plt.bar(labels_estado_civil, sizes_estado_civil, color=colors_estado_civil)
plt.xlabel('Estado Civil')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Mujeres por Estado Civil')
plt.savefig(f'{PathPromedios}mujeres_por_estado_civil_bar_chart.png')  # Save the chart

# 3. Mujeres % por Experiencia
print(f'************************************ Porcentaje de Mujeres por Experiencia ********************************************')
# Asegúrate de que la columna de experiencia sea numérica
FilterSueldoEmpleado[Experiencia] = pd.to_numeric(FilterSueldoEmpleado[Experiencia], errors='coerce')

# Suponiendo que totalMujeres se definió previamente
porcentajeSinExperiencia = (totalSinExperiencia / totalMujeres) * 100
porcentajeMenosAnio = (totalMenosAnio / totalMujeres) * 100
porcentaje1a3 = (total1a3 / totalMujeres) * 100
porcentaje4a6 = (total4a6 / totalMujeres) * 100
porcentaje7a9 = (total7a9 / totalMujeres) * 100
porcentaje10a12 = (total10a12 / totalMujeres) * 100
porcentaje13a15 = (total13a15 / totalMujeres) * 100
porcentaje16a18 = (total16a18 / totalMujeres) * 100
porcentaje19a21 = (total19a21 / totalMujeres) * 100
porcentaje22a24 = (total22a24 / totalMujeres) * 100

# Imprimir resultados
print(f'Porcentaje de Sin Experiencia: {porcentajeSinExperiencia:.2f}%')
print(f'Porcentaje de Menos de un año: {porcentajeMenosAnio:.2f}%')
print(f'Porcentaje de 1 a 3 años: {porcentaje1a3:.2f}%')
print(f'Porcentaje de 4 a 6 años: {porcentaje4a6:.2f}%')
print(f'Porcentaje de 7 a 9 años: {porcentaje7a9:.2f}%')
print(f'Porcentaje de 10 a 12 años: {porcentaje10a12:.2f}%')
print(f'Porcentaje de 13 a 15 años: {porcentaje13a15:.2f}%')
print(f'Porcentaje de 16 a 18 años: {porcentaje16a18:.2f}%')
print(f'Porcentaje de 19 a 21 años: {porcentaje19a21:.2f}%')
print(f'Porcentaje de 22 a 24 años: {porcentaje22a24:.2f}%')

# Crear gráfico de barras para el porcentaje
labels_experiencia = ['Sin Experiencia', 'Menos de un año', '1 a 3 años', '4 a 6 años', '7 a 9 años', 
                      '10 a 12 años', '13 a 15 años', '16 a 18 años', '19 a 21 años', '22 a 24 años']
sizes_experiencia = [porcentajeSinExperiencia, porcentajeMenosAnio, porcentaje1a3, 
                     porcentaje4a6, porcentaje7a9, porcentaje10a12, 
                     porcentaje13a15, porcentaje16a18, porcentaje19a21, porcentaje22a24]

colors_experiencia = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', 
                      '#ffb3e6', '#c2f0c2', '#ff9999', '#ffcc99', '#66ff66']

plt.figure(figsize=(10, 7))
plt.bar(labels_experiencia, sizes_experiencia, color=colors_experiencia)
plt.xlabel('Experiencia')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Mujeres por Experiencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{PathPromedios}mujeres_por_experiencia_bar_chart.png')  # Save the chart


# 4. Mujeres % por Nivel de Instrucción
print(f'************************************ Porcentaje de Mujeres por Nivel de Instrucción ********************************************')
porcentajeNingunoMujeres = (totalNinguno / totalMujeres) * 100
porcentajeCentroAlfaMujeres = (totalCentroAlfa / totalMujeres) * 100
porcentajeJardinInfaMujeres = (totalJardinInfa / totalMujeres) * 100
porcentajeJardinPrimariaMujeres = (totalJardinPrimaria / totalMujeres) * 100
porcentajeEduBasicaMujeres = (totalEduBasica / totalMujeres) * 100
porcentajeSecundariaMujeres = (totalSecundaria / totalMujeres) * 100
porcentajeEducacionMediaMujeres = (totalEducacionMedia / totalMujeres) * 100
porcentajeEducacionSuperiorNoUnivMujeres = (totalEducacionSuperiorNoUniv / totalMujeres) * 100
porcentajeEducacionSuperiorUnivMujeres = (totalEducacionSuperiorUniv / totalMujeres) * 100
porcentajeEducacionPostGradosMujeres = (totalEducacionPostGrados / totalMujeres) * 100

print(f'Porcentaje de Ninguno: {porcentajeNingunoMujeres}')
print(f'Porcentaje de Centro de Alfabetización: {porcentajeCentroAlfaMujeres}')
print(f'Porcentaje de Jardín de Infantes: {porcentajeJardinInfaMujeres}')
print(f'Porcentaje de Jardín de Primaria: {porcentajeJardinPrimariaMujeres}')
print(f'Porcentaje de Educación Básica: {porcentajeEduBasicaMujeres}')
print(f'Porcentaje de Secundaria: {porcentajeSecundariaMujeres}')
print(f'Porcentaje de Educación Media: {porcentajeEducacionMediaMujeres}')
print(f'Porcentaje de Educación Superior No Universitaria: {porcentajeEducacionSuperiorNoUnivMujeres}')
print(f'Porcentaje de Educación Superior Universitaria: {porcentajeEducacionSuperiorUnivMujeres}')
print(f'Porcentaje de Educación de Postgrados: {porcentajeEducacionPostGradosMujeres}')

# Create a bar chart for percentage
labels_instruccion_mujeres = ['Ninguno', 'Centro Alfa', 'Jardín Inf.', 'Jardín Prim.', 'Edu. Básica', 
                      'Secundaria', 'Edu. Media', 'Sup. No Univ.', 'Sup. Univ.', 'Postgrados']
sizes_instruccion_mujeres = [porcentajeNingunoMujeres, porcentajeCentroAlfaMujeres, porcentajeJardinInfaMujeres, porcentajeJardinPrimariaMujeres, porcentajeEduBasicaMujeres, 
                     porcentajeSecundariaMujeres, porcentajeEducacionMediaMujeres, porcentajeEducacionSuperiorNoUnivMujeres, porcentajeEducacionSuperiorUnivMujeres,
                       porcentajeEducacionPostGradosMujeres]
colors_instruccion_mujeres = ['#66b3ff', '#ff9999', '#ffcc99', '#99ff99', '#66ff66', '#ff6666', '#ffcc66', '#c2c2f0', '#ffb3e6', '#c2f0c2']

plt.figure(figsize=(10, 7))
plt.bar(labels_instruccion_mujeres, sizes_instruccion_mujeres, color=colors_instruccion_mujeres)
plt.xlabel('Nivel de Instrucción')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Mujeres por Nivel de Instrucción')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{PathPromedios}mujeres_por_nivel_instruccion_bar_chart.png')
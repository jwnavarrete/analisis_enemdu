import matplotlib.pyplot as plt
from filterData import filtrar_datos

# ESTA FUNCION FILTRA LOS DATOS DE LA BASE DE DATOS DE ENEMDU DE PERSONAS 2023
FilterSueldoEmpleado = filtrar_datos()

#  DEFINIMOS LAS VARIABLES PARA EL ANALISIS
Sexo = 'p02'
Experiencia = 'p45'
Edad = 'p03'
EstadoCivil = 'p06'
Sueldo = 'p66'
Etnia = 'p15' # por validar
NivelInstruccion = 'p10a'
# VARIABLES PARA DEFINIR LOS PATH DE LOS GRAFICOS
PathPorcentajes = 'graficos/porcentajes/'

# 5 PORCENTAJES
# 1. Porcentaje de Hombres y mujeres.
total = len(FilterSueldoEmpleado)

print(f'************************************ Porcentaje de Hombres y Mujeres ********************************************')
totalHombres = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Sexo] == 1])
totalMujeres = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Sexo] == 2])
porcentajeHombres = (totalHombres / total) * 100
porcentajeMujeres = (totalMujeres / total) * 100

print(f'Porcentaje de Hombres: {porcentajeHombres}')
print(f'Porcentaje de Mujeres: {porcentajeMujeres}')

# Crear un gráfico de barras para los porcentajes de hombres y mujeres
labels = ['Hombres', 'Mujeres']
sizes = [porcentajeHombres, porcentajeMujeres]
colors = ['#66b3ff', '#ff9999']

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Sexo')
plt.ylabel('Porcentaje')
plt.title('Porcentajes de Hombres y Mujeres')
plt.savefig(f'{PathPorcentajes}sexo_bar_chart.png')  # Guarda el gráfico como un archivo


# 2. Porcentaje de tipos Estado Civil
print(f'************************************ Porcentaje de Estdos civiles ********************************************')
totalCasados = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 1])
totalSeparado = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 2])
totalDivorciados = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 3])
totalViudos = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 4])
totalUnionLibre = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 5])
totalSolteros = len(FilterSueldoEmpleado[FilterSueldoEmpleado[EstadoCivil] == 6])

porcentajeCasados = (totalCasados / total) * 100
porcentajeSeparado = (totalSeparado / total) * 100
porcentajeDivorciados = (totalDivorciados / total) * 100
porcentajeViudos = (totalViudos / total) * 100
porcentajeUnionLibre = (totalUnionLibre / total) * 100
porcentajeSolteros = (totalSolteros / total) * 100

print(f'Porcentaje de Casados: {porcentajeCasados}')
print(f'Porcentaje de Separados: {porcentajeSeparado}')
print(f'Porcentaje de Divorciados: {porcentajeDivorciados}')
print(f'Porcentaje de Viudos: {porcentajeViudos}')
print(f'Porcentaje de Union Libre: {porcentajeUnionLibre}')
print(f'Porcentaje de Solteros: {porcentajeSolteros}')

# Crear un gráfico circular para los porcentajes de estado civil
labels = ['Casados', 'Separados', 'Divorciados', 'Viudos', 'Union Libre', 'Solteros']
sizes = [porcentajeCasados, porcentajeSeparado, porcentajeDivorciados, porcentajeViudos, porcentajeUnionLibre, porcentajeSolteros]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)  # resaltar el primer segmento

plt.figure(figsize=(10, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # asegurar que el gráfico sea un círculo
plt.title('Porcentajes de Estado Civil')
plt.savefig(f'{PathPorcentajes}estado_civil_pie_chart.png')  # Guarda el gráfico como un archivo

# 3. Porcentaje de tipos de Etnia
print(f'************************************ Porcentaje de Etnia ********************************************')
totalIndigena = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 1])
totalAfro = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 2])
totalNegro = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 3])
totalMulato = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 4])
totalMontubio = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 5])
totalMestizo = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 6])
totalBlanco = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 7])
totalOtro = len(FilterSueldoEmpleado[FilterSueldoEmpleado[Etnia] == 8])

porcentajeIndigena = (totalIndigena / total) * 100
porcentajeAfro = (totalAfro / total) * 100
porcentajeNegro = (totalNegro / total) * 100
porcentajeMulato = (totalMulato / total) * 100
porcentajeMontubio = (totalMontubio / total) * 100
porcentajeMestizo = (totalMestizo / total) * 100
porcentajeBlanco = (totalBlanco / total) * 100
porcentajeOtro = (totalOtro / total) * 100

print(f'Porcentaje de Indigena: {porcentajeIndigena}')
print(f'Porcentaje de Afro: {porcentajeAfro}')
print(f'Porcentaje de Negro: {porcentajeNegro}')
print(f'Porcentaje de Mulato: {porcentajeMulato}')
print(f'Porcentaje de Montubio: {porcentajeMontubio}')
print(f'Porcentaje de Mestizo: {porcentajeMestizo}')
print(f'Porcentaje de Blanco: {porcentajeBlanco}')
print(f'Porcentaje de Otro: {porcentajeOtro}')

# Crear un gráfico de barras para los porcentajes de etnia
labels = ['Indigena', 'Afro', 'Negro', 'Mulato', 'Montubio', 'Mestizo', 'Blanco', 'Otro']
sizes = [porcentajeIndigena, porcentajeAfro, porcentajeNegro, porcentajeMulato, porcentajeMontubio, porcentajeMestizo, porcentajeBlanco, porcentajeOtro]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4']

plt.figure(figsize=(10, 7))
plt.bar(labels, sizes, color=colors)
plt.xlabel('Etnia')
plt.ylabel('Porcentaje')
plt.title('Porcentajes de Etnia')
plt.savefig(f'{PathPorcentajes}etnia_bar_chart.png')  # Guarda el gráfico como un archivo

# calcula 4. Porcentaje de Nivel de instrucción
print(f'************************************ Porcentaje de Nivel de Instrucción ********************************************')
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

porcentajeNinguno = (totalNinguno / total) * 100
porcentajeCentroAlfa = (totalCentroAlfa / total) * 100
porcentajeJardinInfa = (totalJardinInfa / total) * 100
porcentajeJardinPrimaria = (totalJardinPrimaria / total) * 100
porcentajeEduBasica = (totalEduBasica / total) * 100
porcentajeSecundaria = (totalSecundaria / total) * 100
porcentajeEducacionMedia = (totalEducacionMedia / total) * 100
porcentajeEducacionSuperiorNoUniv = (totalEducacionSuperiorNoUniv / total) * 100
porcentajeEducacionSuperiorUniv = (totalEducacionSuperiorUniv / total) * 100
porcentajeEducacionPostGrados = (totalEducacionPostGrados / total) * 100

print(f'Porcentaje de Ninguno: {porcentajeNinguno}')
print(f'Porcentaje de Centro Alfa: {porcentajeCentroAlfa}')
print(f'Porcentaje de Jardin Infantil: {porcentajeJardinInfa}')
print(f'Porcentaje de Jardin Primaria: {porcentajeJardinPrimaria}')
print(f'Porcentaje de Educacion Basica: {porcentajeEduBasica}')
print(f'Porcentaje de Secundaria: {porcentajeSecundaria}')
print(f'Porcentaje de Educacion Media: {porcentajeEducacionMedia}')
print(f'Porcentaje de Educacion Superior No Universitaria: {porcentajeEducacionSuperiorNoUniv}')
print(f'Porcentaje de Educacion Superior Universitaria: {porcentajeEducacionSuperiorUniv}')
print(f'Porcentaje de Educacion Post Grados: {porcentajeEducacionPostGrados}')

# Crear un gráfico de histogramas para los porcentajes de nivel de instrucción
labels = ['Ninguno', 'Centro Alfa', 'Jardin Infantil', 'Jardin Primaria', 'Educacion Basica', 'Secundaria', 'Educacion Media', 'Educacion Superior No Univ', 'Educacion Superior Univ', 'Educacion Post Grados']
sizes = [porcentajeNinguno, porcentajeCentroAlfa, porcentajeJardinInfa, porcentajeJardinPrimaria, porcentajeEduBasica, porcentajeSecundaria, porcentajeEducacionMedia, porcentajeEducacionSuperiorNoUniv, porcentajeEducacionSuperiorUniv, porcentajeEducacionPostGrados]

plt.figure(figsize=(12, 8))
plt.bar(labels, sizes, color='skyblue')
plt.xlabel('Nivel de Instrucción')
plt.ylabel('Porcentaje')
plt.title('Histogramas de Porcentajes de Nivel de Instrucción')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'{PathPorcentajes}nivel_instruccion_histograma.png')  # Guarda el gráfico como un archivo

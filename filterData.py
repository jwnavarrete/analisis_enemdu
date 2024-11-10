import pandas as pd

def filtrar_datos():
    # Leer el archivo CSV
    csv_path = 'base/enemdu_persona_2024_07.csv'
    delimiter = ';'
    mes=1
    sueldo_min=550 
    sueldo_max=3500
    # 
    df = pd.read_csv(csv_path, delimiter=delimiter, low_memory=False)
    
    # Definir las variables para el análisis
    Mes = 'mes'
    Experiencia = 'p45'
    Sueldo = 'p66'
    EstadoCivil = 'p06'
    Edad = 'p06'
    Etnia = 'p15'
    NivelInstruccion = 'p10a'

    # Filtrar el DataFrame para que solo sean los datos del mes que nos interesa
    # filteredMes = df[df[Mes] == mes]
    filteredMes = df
    
    # Limpiar la columna Sueldo: eliminar espacios en blanco o reemplazarlos por NaN
    filteredMes[Sueldo] = filteredMes[Sueldo].replace(' ', None)
    
    # Convertir a numérico toda la columna Sueldo, errores se manejarán con 'coerce' (convertir errores a NaN)
    filteredMes[Sueldo] = pd.to_numeric(filteredMes[Sueldo], errors='coerce')

    
    
    # Filtrar los datos para que solo sean los que tengan un sueldo entre sueldo_min y sueldo_max
    FilterSueldoEmpleado = filteredMes[(filteredMes[Sueldo] >= sueldo_min) & (filteredMes[Sueldo] <= sueldo_max)]
    
    # Crear y agregar una variable llamada Bono que contenga el siguiente cálculo:
    # 𝐁𝐨𝐧𝐨 = [(𝒔𝒖𝒆𝒍𝒅𝒐 𝒙 𝟎.𝟎𝟏𝟐 𝒙 𝑬𝒙𝒑𝒆𝒓𝒊𝒆𝒏𝒄𝒊𝒂) + 𝒔𝒖𝒆𝒍𝒅𝒐]
    # Convertir la columna Experiencia a numérico, errores se manejarán con 'coerce' (convertir errores a NaN)
    FilterSueldoEmpleado[Experiencia] = pd.to_numeric(FilterSueldoEmpleado[Experiencia], errors='coerce')
    
    # CONVERTIR A NUMÉRICO LA COLUMNA EstadoCivil
    FilterSueldoEmpleado[EstadoCivil] = pd.to_numeric(FilterSueldoEmpleado[EstadoCivil], errors='coerce')

    # convertir a numérico la columna Etnia
    FilterSueldoEmpleado[Etnia] = pd.to_numeric(FilterSueldoEmpleado[Etnia], errors='coerce')

    # convertir a numérico la columna NivelInstruccion
    FilterSueldoEmpleado[NivelInstruccion] = pd.to_numeric(FilterSueldoEmpleado[NivelInstruccion], errors='coerce')

    # Calcular el Bono
    FilterSueldoEmpleado['Bono'] = (FilterSueldoEmpleado[Sueldo] * 0.012 * FilterSueldoEmpleado[Experiencia]) + FilterSueldoEmpleado[Sueldo]
    # Convertir la columna Bono a numérico, errores se manejarán con 'coerce' (convertir errores a NaN)

    # QUIERO que la base solo tenga las columnas mes, p02, p45, p66, p06, p15, p10a y Bono
    FilterSueldoEmpleado = FilterSueldoEmpleado[['p02', 'p03', 'p45', 'p66', 'p06', 'p15', 'p10a', 'Bono']]

    # Guardar los datos filtrados en un archivo CSV en la ruta ./base
    FilterSueldoEmpleado.to_csv(f'base/FilterSueldoEmpleado.csv', index=False, sep=';')
    
    return FilterSueldoEmpleado

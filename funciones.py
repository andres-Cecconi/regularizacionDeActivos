def promedio_edad(usuarios):
    suma_edades = 0
    for usuario in usuarios:
        suma_edades += usuario[3]
    return suma_edades / len(usuarios)

def edad_minima(usuarios):
    edad_min = usuarios[0][3]
    for usuario in usuarios:
        if usuario[3] < edad_min:
            edad_min = usuario[3]
    return edad_min

def edad_maxima(usuarios):
    edad_max = usuarios[0][3]
    for usuario in usuarios:
        if usuario[3] > edad_max:
            edad_max = usuario[3]
    return edad_max

def fecha_declaracion_mas_antigua(usuarios):
    fecha_mas_antigua = usuarios[0][6]
    for usuario in usuarios:
        if usuario[6] < fecha_mas_antigua:
            fecha_mas_antigua = usuario[6]
    return fecha_mas_antigua

def fecha_declaracion_mas_reciente(usuarios):
    fecha_mas_reciente = usuarios[0][6]
    for usuario in usuarios:
        if usuario[6] > fecha_mas_reciente:
            fecha_mas_reciente = usuario[6]
    return fecha_mas_reciente

def menor_monto(usuarios):
    menor_monto = usuarios[0][9]
    for usuario in usuarios:
        if usuario[9] < menor_monto:
            menor_monto = usuario[9]
    return menor_monto

def mayor_monto(usuarios):
    mayor_monto = usuarios [0][9]
    for usuario in usuarios:
        if usuario[9] > mayor_monto:
            mayor_monto = usuario[9]
    return mayor_monto

def monto_promedio(usuarios):
    suma_montos = 0
    for usuario in usuarios:
        suma_montos += usuario[9]
    return suma_montos / len(usuarios)


def activo_mas_repetido(usuarios):
    # Extraer todos los bienes en una lista
    lista_bienes = [usuario[8] for usuario in usuarios]  

    # Crear una lista única de bienes
    bienes_unicos = []
    for bien in lista_bienes:
        if bien not in bienes_unicos:
            bienes_unicos.append(bien)

    # Contar la frecuencia de cada bien
    conteos = []
    for bien in bienes_unicos:
        conteos.append(lista_bienes.count(bien))

    # Encontrar el índice del bien más repetido
    max_frecuencia = 0
    indice_mas_repetido = 0
    for i in range(len(conteos)):
        if conteos[i] > max_frecuencia:
            max_frecuencia = conteos[i]
            indice_mas_repetido = i

    # Devolver el bien más repetido y su frecuencia
    return bienes_unicos[indice_mas_repetido], max_frecuencia


def activo_menos_repetido(usuarios):
    # Extraer todos los bienes en una lista
    lista_bienes = [usuario[8] for usuario in usuarios]

    # Crear una lista única de bienes
    bienes_unicos = []
    for bien in lista_bienes:
        if bien not in bienes_unicos:
            bienes_unicos.append(bien)

    # Contar la frecuencia de cada bien
    conteos = []
    for bien in bienes_unicos:
        conteos.append(lista_bienes.count(bien))

    # Encontrar el índice del bien menos repetido
    min_frecuencia = conteos[0]
    indice_menos_repetido = 0
    for i in range(len(conteos)):
        if conteos[i] < min_frecuencia:
            min_frecuencia = conteos[i]
            indice_menos_repetido = i

    # Devolver el bien menos repetido y su frecuencia
    return bienes_unicos[indice_menos_repetido], min_frecuencia


def profesion_mas_elegida(usuarios):
    # Extraer todas las profesiones en una lista
    lista_profesiones = [usuario[5] for usuario in usuarios]

    # Crear una lista única de profesiones
    profesiones_unicas = []
    for profesion in lista_profesiones:
        if profesion not in profesiones_unicas:
            profesiones_unicas.append(profesion)

    # Contar la frecuencia de cada profesion
    conteos = []
    for profesion in profesiones_unicas:
        conteos.append(lista_profesiones.count(profesion))

    # Encontrar el índice de la profesion más elegida
    max_frecuencia = 0
    indice_mas_elegida = 0
    for i in range(len(conteos)):
        if conteos[i] > max_frecuencia:
            max_frecuencia = conteos[i]
            indice_mas_elegida = i

    # Devolver la profesion mas elegida y su frecuencia
    return profesiones_unicas[indice_mas_elegida], max_frecuencia

def origen_fondos_mas_elegido(usuarios):
    # Extraer todos los orgienes de fondos en una lista
    lista_origenes_fondos = [usuario[10] for usuario in usuarios]  

    # Crear una lista única de orgienes de fondos
    origenes_fondos_unicos = []
    for origen_fondos in lista_origenes_fondos:
        if origen_fondos not in origenes_fondos_unicos:
            origenes_fondos_unicos.append(origen_fondos)

    # Contar la frecuencia de cada origen de fondos
    conteos = []
    for origen_fondos in origenes_fondos_unicos:
        conteos.append(lista_origenes_fondos.count(origen_fondos))

    # Encontrar el índice del origen de fondos más elegido
    max_frecuencia = 0
    indice_mas_elegido = 0
    for i in range(len(conteos)):
        if conteos[i] > max_frecuencia:
            max_frecuencia = conteos[i]
            indice_mas_elegido = i

    # Devolver el origen de fondos mas elegido y su frecuencia
    return origenes_fondos_unicos[indice_mas_elegido], max_frecuencia


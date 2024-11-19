def calcular_edad_minima (edades):
    
    edad_minima = edades[0]
    
    for i in edades:
        if i < edad_minima:
            edad_minima = i
            
    return edad_minima


def calcular_edad_maxima (edades):
    
    edad_maxima = edades[0]
    
    for i in edades:
        if i > edad_maxima:
            edad_maxima = i
            
    return edad_maxima



def calcular_promedio_edades (edades):
    
    total_edades = 0
    
    for i in edades:
        total_edades += i
        
    return total_edades / len(edades) # contemplar caso de division por cero



def calcular_fecha_declaraciones_cercana (fechas_declaraciones):
    
    fecha_cercana = fechas_declaraciones[0]
    
    for i in fechas_declaraciones:
        if i > fecha_cercana:
            fecha_cercana = i
            
    return fecha_cercana


def calcular_fecha_declaraciones_lejana (fechas_declaraciones):
    
    fecha_lejana = fechas_declaraciones[0]
    
    for i in fechas_declaraciones:
        if i < fecha_lejana:
            fecha_lejana = i
            
    return fecha_lejana


def calcular_monto_minimo (monto_declaraciones):
    
    monto_minimo = monto_declaraciones[0]
    
    
    for i in monto_declaraciones:
        if i < monto_minimo:
            monto_minimo = i
            
    return monto_minimo


def calcular_monto_maximo(monto_declaraciones):
    monto_maximo = monto_declaraciones[0]

    for i in monto_declaraciones: # cambiar el nombre de la variable i por monto
        if i > monto_maximo:
            monto_maximo = i
            
    return monto_maximo


def calcular_promedio_montos (monto_declaraciones):
    
    total_montos = 0
    
    for i in monto_declaraciones:
        total_montos += i
        
    return total_montos / len(monto_declaraciones)

def calcular_ranking(lista):
    ranking = []
    for item in lista:
        encontrado = False
        for registro in ranking:
            if registro[0] == item:
                registro[1] += 1
                encontrado = True
        if not encontrado:
            ranking.append([item, 1])
    return ranking





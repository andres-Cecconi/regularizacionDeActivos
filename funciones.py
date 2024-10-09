def calcular_edad_minima_maxima (edades):
    
    edad_minima = edades[0]
    edad_maxima = edades[0]
    
    for i in edades:
        if i < edad_minima:
            edad_minima = i
        if i > edad_maxima:
            edad_maxima = i
            
    return edad_minima, edad_maxima



def calcular_promedio_edades (edades):
    
    total_edades = 0
    
    for i in edades:
        total_edades += i
        
    return total_edades / len(edades)



def calcular_fecha_declaraciones_cercana_lejana (fechas_declaraciones):
    
    fecha_lejana = fechas_declaraciones[0]
    fecha_cercana = fechas_declaraciones[0]
    
    for i in fechas_declaraciones:
        if i < fecha_lejana:
            fecha_lejana = i
        if i > fecha_cercana:
            fecha_cercana = i
            
    return fecha_cercana, fecha_lejana


def calcular_monto_minimo_maximo (monto_declaraciones):
    
    monto_minimo = monto_declaraciones[0]
    monto_maximo = monto_declaraciones[0]
    
    for i in monto_declaraciones:
        if i < monto_minimo:
            monto_minimo = i
        if i > monto_maximo:
            monto_maximo = i
            
    return monto_minimo, monto_maximo



def calcular_promedio_montos (monto_declaraciones):
    
    total_montos = 0
    
    for i in monto_declaraciones:
        total_montos += i
        
    return total_montos / len(monto_declaraciones)




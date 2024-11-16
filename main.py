from funciones import *

print("Bienvenido al Sistema de Regularización de Activos")

def validar_edad(edad):
    while edad < 18:
        print("No se permiten menores de edad")
        edad = int(input("Por favor ingrese su edad (ingresar obligatoriamente enteros): "))
    return edad


def obtener_profesion():
    print(profesiones_listadas)
    respuesta = input("Ingrese el número de la profesión o escriba su profesión si no está en la lista: ")
    
    es_numero = True
    for caracter in respuesta:
        if caracter < '0' or caracter > '9':
            es_numero = False
            break
    
    if es_numero:
        numero_ingresado = int(respuesta)
        if 1 <= numero_ingresado <= len(profesiones):
            profesion_seleccionada = profesiones[numero_ingresado - 1]
            return profesion_seleccionada
        else:
            print("La profesión no está en la lista.")
    else:
        profesion_manual = respuesta
        return profesion_manual
    

def obtener_origen_fondo():
    print(origenes_fondos_listados)
    respuesta = input("Ingrese el número del origen de fondo o escriba su origen de fondo si no está en la lista: ")
    
    es_numero = True
    for caracter in respuesta:
        if caracter < '0' or caracter > '9':
            es_numero = False
            break
    
    if es_numero:
        numero_ingresado = int(respuesta)
        if 1 <= numero_ingresado <= len(origenes_fondos):
            origen_fondo_seleccionado = origenes_fondos[numero_ingresado - 1]
            return origen_fondo_seleccionado
        else:
            print("El origen de fondo no está en la lista.")
    else:
        origen_fondo_manual = respuesta
        return origen_fondo_manual
    


edades = []
profesiones = []
fechas_declaraciones = []
monto_declaraciones = []
origen_fondos = []
profesiones = [
    "Abogado/a", "Contador/a Público", "Médico/a", "Ingeniero/a", "Arquitecto/a",
    "Docente/Profesor/a", "Psicólogo/a", "Diseñador/a Gráfico/a", "Farmacéutico/a",
    "Veterinario/a", "Enfermero/a", "Kinesiólogo/a", "Odontólogo/a", "Economista",
    "Periodista/Comunicador/a Social", "Técnico/a en Informática/Programador/a", 
    "Electricista", "Carpintero/a", "Plomero/a", "Chef/Gastrónomo/a",
    "Piloto/a de Aviación", "Actor/Actriz", "Artista Plástico/a", "Fotógrafo/a", 
    "Músico/a", "Empleado/a Administrativo/a", "Comerciante", "Ingeniero/a Agrónomo/a", 
    "Traductor/a", "Técnico/a en Construcción", "Operario/a de Fábrica", 
    "Analista de Sistemas", "Científico/a/Investigador/a", "Marketing/Publicidad", 
    "Deportista Profesional", "Agente Inmobiliario", "Soldador/a", 
    "Operador/a de Maquinaria Pesada", "Mecánico/a Automotor", "Peluquero/a/Estilista"
]

profesiones_listadas = """
    1. Abogado/a
    2. Contador/a Público
    3. Médico/a
    4. Ingeniero/a 
    5. Arquitecto/a 
    6. Docente/Profesor/a 
    7. Psicólogo/a
    8. Diseñador/a Gráfico/a
    9. Farmacéutico/a 
    10. Veterinario/a 
    11. Enfermero/a
    12. Kinesiólogo/a 
    13. Odontólogo/a
    14. Economista
    15. Periodista/Comunicador/a Social 
    16. Técnico/a en Informática/Programador/a
    17. Electricista
    18. Carpintero/a
    19. Plomero/a
    20. Chef/Gastrónomo/a 
    21. Piloto/a de Aviación
    22. Actor/Actriz
    23. Artista Plástico/a 
    24. Fotógrafo/a
    25. Músico/a
    26. Empleado/a Administrativo/a
    27. Comerciante
    28. Ingeniero/a Agrónomo/a
    29. Traductor/a
    30. Técnico/a en Construcción
    31. Operario/a de Fábrica
    32. Analista de Sistemas
    33. Científico/a/Investigador/a
    34. Marketing/Publicidad
    35. Deportista Profesional
    36. Agente Inmobiliario
    37. Soldador/a
    38. Operador/a de Maquinaria Pesada 
    39. Mecánico/a Automotor 
    40. Peluquero/a/Estilista

"""
frecuencias = [0] * len(profesiones)                    

origenes_fondos = [
    "Ingresos laborales",
    "Inversiones financieras",
    "Herencia",
    "Donación"
]
origenes_fondos_listados = """
    1 - Ingresos laborales
    2 - Inversiones financieras
    3 - Herencia
    4 - Donación
    5 - Ninguno de los anteriores (salir)
"""

contador = 0
estado = True

while estado == True: 
    contribuyente = input("Por favor ingrese N para ingresar un nuevo contribuyente (o S para salir): ")
    if contribuyente == "N" or contribuyente == "n":
        contador += 1
        
        dni = input("Por favor ingrese su DNI (sin caracteres especiales y maximo 8 digitos): ")
        while len(dni) > 8 or len(dni) < 7:
            print("El DNI debe tener un maximo de 8 digitos y un minimo de 6 digitos")
            dni = input("Por favor ingrese su DNI (sin caracteres especiales y maximo 8 digitos): ")

        apellido = input("Por favor ingrese su apellido: ")

        nombre = input("Por favor ingrese su nombre: ")

        #Ingresar obligatoriamente en formato entero ya que no es posible validar que no se ingresen letras
        edad = validar_edad(int(input("Por favor ingrese su edad (ingresar obligatoriamente enteros): ")))

        fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        while len(fecha_nacimiento) != 10:
            print("La fecha de nacimiento no es valida (respetar formato para ingresar la fecha)")
            fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (DD/MM/AAAA): ")

        profesion_seleccionada = obtener_profesion()
        print("La profesión seleccionada es:", profesion_seleccionada)

        for i in range(len(profesiones)):
            for j in range (i + 1, len(profesiones)):
                if frecuencias[i] == frecuencias[j]:
                    #intermcio de profesiones y frecuencias
                    profesion_temporal = profesiones[i]
                    profesiones[i] = profesiones[j]
                    profesiones[j] = profesion_temporal
                    frecuencia_temporal = frecuencias[i]
                    frecuencias[i] = frecuencias[j]
                    frecuencias[j] = frecuencia_temporal

        fecha_declaracion = input("Por favor ingrese la fecha de la declaración (DD/MM/AAAA): ")
        while len(fecha_declaracion) != 10:
            print("La fecha de la declaración no es valida (respetar formato para ingresar la fecha)")
            fecha_declaracion = input("Por favor ingrese la fecha de la declaración (DD/MM/AAAA): ")
        
        #Ingresar obligatoriamente numeros ya que no es posible validar que no se ingresen letras
        monto_declarar = float(input("Por favor ingrese el monto a declarar (ingresar obligatoriamente numeros): "))
        while monto_declarar <= 0:
            print("Monto invalido, por favor ingrese un monto mayor a 0")
            monto_declarar = float(input("Por favor ingrese el monto a declarar (ingresar obligatoriamente numeros): "))

        # origen_fondo = input("Por favor ingrese el origen de los fondos (no se permiten fondos de origen ilícito): ")
        origen_fondo = obtener_origen_fondo()
        print("El origen de los fondos es:", origen_fondo)

        edades.append(edad)
        profesiones.append(profesion_seleccionada)
        fechas_declaraciones.append(fecha_declaracion)
        monto_declaraciones.append(monto_declarar)
        origen_fondos.append(origen_fondo)

    elif contribuyente == "S" or contribuyente == "s":
        print("Hasta la próxima")
        estado = False
        
        if contador > 0:
            
            print("La cantidad de contribuyentes registrados es:", contador)
            print("La menor edad registrada es:", calcular_edad_minima(edades))
            print("La mayor edad registrada es:", calcular_edad_maxima(edades))
            print("El promedio de las edades registradas es:", calcular_promedio_edades(edades))
            print("La fecha de declaración más cercana registrada es:", calcular_fecha_declaraciones_cercana(fechas_declaraciones))
            print("La fecha de declaración más lejana registrada es:", calcular_fecha_declaraciones_lejana(fechas_declaraciones))
            print("El menor monto registrado es:", calcular_monto_minimo(monto_declaraciones))
            print("El mayor monto registrado es:", calcular_monto_maximo(monto_declaraciones))
            print("El promedio de los montos registrados es:", calcular_promedio_montos(monto_declaraciones))
            print("Ranking de las profesiones más seleccionadas:")
            for i in range(len(profesiones)):   
                print(f"{profesiones[i]}: {frecuencias[i]} veces")
            for i in range(contador):
                    print("El origen de los fondos del contribuyente", i+1, "es:", origen_fondos[i])
            
            print("Gracias por utilizar el sistema")
    else:
        print("Por favor ingrese un valor válido")


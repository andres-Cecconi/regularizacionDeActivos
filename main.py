from funciones import *

print("Aquí habrá un programa para regularizar activos")

edades = []
profesiones = []
fechas_declaraciones = []
monto_declaraciones = []
origen_fondos = []
contador = 0

estado = True

while estado == True:
    contribuyente = input("Por favor ingrese N para nuevo contribuyente (o S para salir): ")
    if contribuyente == "N" or contribuyente == "n":
        
        contador += 1
        
        dni = input("Por favor ingrese su DNI (sin caracteres especiales y maximo 8 digitos): ")
        while len(dni) > 8 or len(dni) < 7:
            print("El DNI debe tener un maximo de 8 digitos y un minimo de 6 digitos")
            dni = input("Por favor ingrese su DNI (sin caracteres especiales y maximo 8 digitos): ")
        apellido = input("Por favor ingrese su apellido: ")
        nombre = input("Por favor ingrese su nombre: ")
        #Ingresar obligatoriamente en formato entero ya que no es posible validar que no se ingresen letras
        edad = int(input("Por favor ingrese su edad (ingresar obligatoriamente enteros): "))
        while edad < 18:
            print("No se permiten menores de edad")
            edad = int(input("Por favor ingrese su edad (ingresar obligatoriamente enteros): "))
        fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        while len(fecha_nacimiento) != 10:
            print("La fecha de nacimiento no es valida (respetar formato para ingresar la fecha)")
            fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        
        profesiones_listadas = """
        1 - Abogado/a
        2 - Médico/a
        3 - Contador/a
        4 - Ingeniero/a (en diversas ramas: civil, industrial, sistemas, etc.)
        5 - Arquitecto/a
        6 - Psicólogo/a
        7 - Enfermero/a
        8 - Licenciado/a en Administración
        9 - Profesor/a
        10 - Diseñador/a Gráfico/a
        11 - Periodista
        12 - Farmacéutico/a
        13 - Veterinario/a
        14 - Técnico/a en Informática
        15 - Trabajador/a Social
        16 - Electricista
        17 - Chef
        18 - Diseñador/a Industrial
        19 - Técnico/a en Construcción
        20 - Sastre/a
        21 - Estilista/Peluquero/a
        22 - Traductor/a
        23 - Técnico/a en Higiene y Seguridad en el Trabajo
        24 - Guía de Turismo
        25 - Músico/a
        26 - Actor/Actriz
        27 - Productor/a de Eventos
        28 - Cocinero/a
        29 - Carpintero/a
        30 - Albañil
        31 - Ingeniero/a en Sistemas
        32 - Fisioterapeuta
        33 - Nutricionista
        34 - Fonoaudiólogo/a
        35 - Oftalmólogo/a
        36 - Odontólogo/a
        37 - Líder de Ventas/Vendedor/a
        38 - Perito/a
        39 - Notario/a
        40 - Coach Personal o Empresarial
        41 - Consultor/a
        42 - Científico/a
        43 - Matemático/a
        44 - Analista de Datos
        45 - Bioquímico/a
        46 - Antropólogo/a
        47 - Técnico/a en Energías Renovables
        48 - Decorador/a de Interiores
        49 - Asesor/a Financiero/a
        50 - Investigador/a
        51 - Programador/a
        52 - Técnico/a en Logística
        53 - Artista Plástico/a
        54 - Cineasta
        55 - Licenciado/a en Relaciones Públicas
        56 - Operador/a de Radio
        57 - Estilista de Moda
        58 - Diseñador/a de Moda
        59 - Maestro/a de Obras
        60 - Técnico/a en Redes y Telecomunicaciones
        """
        print(profesiones_listadas)
        profesion = input("Por favor ingrese el número correspondiente a su profesión: ")
        fecha_declaracion = input("Por favor ingrese la fecha de la declaración (DD/MM/AAAA): ")
        while len(fecha_declaracion) != 10:
            print("La fecha de la declaración no es valida (respetar formato para ingresar la fecha)")
            fecha_declaracion = input("Por favor ingrese la fecha de la declaración (DD/MM/AAAA): ")
        #Ingresar obligatoriamente numeros ya que no es posible validar que no se ingresen letras
        monto_declarar = float(input("Por favor ingrese el monto a declarar (ingresar obligatoriamente numeros): "))
        while monto_declarar <= 0:
            print("No se permite ese monto")
            monto_declarar = float(input("Por favor ingrese el monto a declarar (ingresar obligatoriamente numeros): "))
        origen_fondo = input("Por favor ingrese el origen de los fondos (no se permiten fondos de origen ilícito): ")

        edades.append(edad)
        profesiones.append(profesion)
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
            for i in range(contador):
                print("La profesión del contribuyente", i+1, "es:", profesiones[i])
                print("El origen de los fondos del contribuyente", i+1, "es:", origen_fondos[i])
            
    
    else:
        print("Por favor ingrese un valor válido")


from funciones import *

# Variables
usuarios = []  # Lista de usuarios, cada usuario es una lista con los datos de cada usuario (nombre [0], apellido [1], dni [2], edad [3], fecha de nacimiento [4], profesion [5], fecha de declaración [6], radicación de bienes [7], bienes [8], monto [9], origen de fondos [10])
profesiones_listadas = [
    "Abogado/a",
    "Agente Inmobiliario/a",
    "Arquitecto/a",
    "Auditor/a",
    "Consultor/a",
    "Contador/a",
    "Corredor/a de Comercio",
    "Diseñador/a Gráfico/a",
    "Economista",
    "Empresario/a"
    "Escribano/a",
    "Especialista en Tributación",
    "Gestor/a de Proyectos",
    "Ingeniero/a",
    "Médico/a",
    "Odontólogo/a",
    "Programador/a",
    "Psicólogo/a",
    "Veterinario/a",
]


origenes_fondos_listados = origenes_fondos = [
    "Ingresos no declarados previamente",
    "Ingresos derivados de actividades informales o no registradas",
    "Rendimientos de bienes no declarados",
    "Fondos provenientes de la venta de bienes no declarados",
    "Fondos obtenidos en el exterior",
    "Donaciones no informadas",
    "Incorporación de bienes de origen lícito",
    "Préstamos informales o no documentados",
    "Herencias y sucesiones"
]

radicacion_bienes_listados = [
    "Argentina", 
    "Exterior"
]

bienes_listados = [
    "Moneda extranjera", 
    "Inmuebles", 
    "Participacion en sociedades o cuotapartes de FCI", 
    "Titulos valores", 
    "Criptomonedas"
]

estado = True
contador_usuarios = 0

while estado == True:
    nuevo_usuario = input("Desea ingresar un nuevo usuario? (si/no): ")
    if nuevo_usuario == "no":
        estado = False  

        if contador_usuarios > 0:
            print ("Cantidad de usuarios ingresados: ", contador_usuarios)
            print("Estadísticas de los usuarios:")
            edad_min = edad_minima(usuarios)
            print(f"La menor edad registrada es de {edad_min} años")
            edad_max = edad_maxima(usuarios)
            print(f"La mayor edad registrada es de {edad_max} años")
            edad_prom = promedio_edad(usuarios)
            print(f"El promedio de edad de los usuarios registrados es de  {edad_prom} años")
            fecha_mas_antigua = fecha_declaracion_mas_antigua(usuarios)
            print(f"La fecha de declaración más antigua es {fecha_mas_antigua}")
            fecha_mas_reciente = fecha_declaracion_mas_reciente(usuarios)
            print(f"La fecha de declaración más reciente es {fecha_mas_reciente}")
            monto_min = menor_monto(usuarios)
            print(f"El monto más bajo declarado es de {monto_min} dólares")
            monto_max = mayor_monto(usuarios)
            print(f"El monto más alto declarado es de {monto_max} dólares")
            monto_prom = monto_promedio(usuarios)
            print(f"El monto promedio declarado es de {monto_prom} dólares")
            bien_mas_repetido, cantidad = activo_mas_repetido(usuarios)
            print(f"El bien más repetido es '{bien_mas_repetido}' y aparece {cantidad} veces.")
            bien_menos_repetido, cantidad_menos_repetido = activo_menos_repetido(usuarios)
            print(f"El bien menos repetido es '{bien_menos_repetido}' y aparece {cantidad_menos_repetido} veces.")
            profesion_top, cantidad = profesion_mas_elegida(usuarios)
            print(f"La profesion mas elegida es '{profesion_top}' y aparece {cantidad} veces.")
            origen_fondos_top, cantidad = origen_fondos_mas_elegido(usuarios)
            print(f"El origen de fondos mas elegido es '{origen_fondos_top}' y aparece {cantidad} veces.")
            print("------------------------------")

        buscar_usuario = "si"
        while buscar_usuario == "si":
            buscar_usuario = input("Desea buscar los datos de algún contribuyente en particular? (si/no): ")
            if buscar_usuario == "no":
                break
            elif buscar_usuario == "si":
                dni_buscar = input("Ingrese el dni del usuario que desea buscar: ")
                encontrado = False
                for usuario in usuarios:
                    if usuario[2] == int(dni_buscar):
                        print(f"Nombre: {usuario[0]}")
                        print(f"Apellido: {usuario[1]}")
                        print(f"DNI: {usuario[2]}")
                        print(f"Edad: {usuario[3]}")
                        print(f"Fecha de nacimiento: {usuario[4]}")
                        print(f"Fecha de declaración: {usuario[5]}")
                        print(f"Profesión: {usuario[6]}")
                        print(f"Radicación de bienes: {usuario[7]}")
                        print(f"Bienes: {usuario[8]}")
                        print(f"Monto: {usuario[9]}")
                        print(f"Origen de los fondos: {usuario[10]}")
                        print("------------------------------")
                        encontrado = True
                        break
                if not encontrado:
                    print("No se encontraron datos del contribuyente con ese DNI, por favor, verifique el DNI ingresado.")

            print("------------------------------")
            print("Gracias por utilizar nuestros servicios!")
        else:
            print("No se ingresaron usuarios")
            print ("Gracias por utilizar nuestros servicios!")

    elif nuevo_usuario == "si":
        contador_usuarios +=1

        nombre_usuario = input("Ingrese el nombre del usuario: ")
        while not nombre_usuario:
            print("Por favor, ingrese un nombre válido.")
            nombre_usuario = input("Ingrese el nombre del usuario: ")

        apellido_usuario = input("Ingrese el apellido del usuario: ")
        while not apellido_usuario:
            print("Por favor, ingrese un apellido válido.")
            apellido_usuario = input("Ingrese el apellido del usuario: ")

        dni_usuario = int(input("Ingrese el DNI del usuario: "))
        while (dni_usuario < 1000000 or dni_usuario > 99999999):
            print("Por favor, ingrese un DNI válido.")
            dni_usuario = int(input("Ingrese el DNI del usuario: "))
        
        edad_usuario = int(input("Ingrese la edad del usuario: "))
        while (edad_usuario < 18):
            print("No se permite el registro de menores de edad. Por favor, ingrese una edad válida.")
            edad_usuario = int(input("Ingrese la edad del usuario: "))
        
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del usuario (dd/mm/aaaa): ")
        while not fecha_nacimiento or len(fecha_nacimiento) != 10:
            print("Por favor, ingrese una fecha válida.")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del usuario (dd/mm/aaaa): ")

        print(profesiones_listadas)
        profesion_usuario = input("Ingrese su profesion de acuerdo a la lista: ")
        while profesion_usuario not in profesiones_listadas:
            print("Por favor, ingrese una profesión válida.")
            profesion_usuario = input("Ingrese su profesion de acuerdo a la lista: ")
        
        fecha_declaracion = input("Ingrese la fecha de declaración de usuario (dd/mm/aaaa): ")
        while not fecha_declaracion or len(fecha_declaracion) !=10:
            print("Por favor, ingrese una fecha válida.")
            fecha_declaracion = input("Ingrese la fecha de declaración de usuario (dd/mm/aaaa): ")

        print(radicacion_bienes_listados)
        radicacion_bienes = input("Ingrese la radicación de los bienes: ")
        while radicacion_bienes not in radicacion_bienes_listados:
            print("Por favor, ingrese una radicación de bienes válida.")
            radicacion_bienes = input("Ingrese la radicación de los bienes: ")

        print(bienes_listados)
        bienes = input("Ingrese los bienes que posee: ")
        while bienes not in bienes_listados:
            print("Por favor, ingrese un bien válido.")
            bienes = input("Ingrese los bienes que posee: ")
        
        monto = float(input("Ingrese el monto en dólares de los bienes a regularizar: "))
        while not monto or (monto < 0):
            print("Por favor, ingrese un monto válido.")
            monto = float(input("Ingrese el monto en dólares que quiere regularizar: "))
        
        print(origenes_fondos_listados)
        origen_fondos = input("Ingrese el origen de los fondos de acuerdo a la lista: ")
        while origen_fondos not in origenes_fondos_listados:
            print("Por favor, ingrese un origen de fondos válido.")
            origen_fondos = input("Ingrese el origen de los fondos de acuerdo a la lista: ")

        usuario = [nombre_usuario, apellido_usuario, dni_usuario, edad_usuario, fecha_nacimiento, profesion_usuario, fecha_declaracion, radicacion_bienes, bienes, monto, origen_fondos]
        usuarios.append(usuario)



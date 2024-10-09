print("Aqui habra un programa para regularizar activos")

dnis = []
apellidos = []
nombres = []
edads = []
fecha_nacimientos = []
profesiones = []
fecha_declaraciones = []
monto_declaraciones = []
origen_fondos = []

estado = True

while (estado == True):
    contribuyente = input("Por favor ingrese N para nuevo contribuyente (o S para salir): ")
    if contribuyente == "N":
        dni = input("Por favor ingrese su dni: ")
        apellido = input("Por favor ingrese su apellido: ")
        nombre = input("Por favor ingrese su nombre: ")
        edad = int(input("Por favor ingrese su edad: "))
        fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento: ")
        profesion = input("Por favor ingrese su profesion: ")
        fecha_declaracion = input("Por favor ingrese la fecha de la declaracion: ")
        monto_declarar = int(input("Por favor ingrese el monto a declarar: "))
        origen_fondo = input("Por favor ingrese el origen de fondos: ")
        
        dnis.append(dni)
        apellidos.append(apellido)
        nombres.append(nombre)
        edads.append(edad)
        fecha_nacimientos.append(fecha_nacimiento)
        profesiones.append(profesion)
        fecha_declaraciones.append(fecha_declaracion)
        monto_declaraciones.append(monto_declarar)
        origen_fondos.append(origen_fondo)
    elif contribuyente == "S":
        print("Hasta la proxima")
        estado = False
        print(dnis)
        print(apellidos)
        print(nombres)
        print(edads)
        print(fecha_nacimientos)
        print(profesiones)
        print(fecha_declaraciones)
        print(monto_declaraciones)
        print(origen_fondos)
    else:
        print("Por favor ingrese un valor valido")

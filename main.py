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
        
        dni = input("Por favor ingrese su DNI: ")
        apellido = input("Por favor ingrese su apellido: ")
        nombre = input("Por favor ingrese su nombre: ")
        edad = int(input("Por favor ingrese su edad: "))
        fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        profesion = input("Por favor ingrese su profesión: ")
        fecha_declaracion = input("Por favor ingrese la fecha de la declaración (DD/MM/AAAA): ")
        monto_declarar = int(input("Por favor ingrese el monto a declarar: "))
        origen_fondo = input("Por favor ingrese el origen de los fondos: ")

        edades.append(edad)
        profesiones.append(profesion)
        fechas_declaraciones.append(fecha_declaracion)
        monto_declaraciones.append(monto_declarar)
        origen_fondos.append(origen_fondo)

    elif contribuyente == "S" or contribuyente == "s":
        print("Hasta la próxima")
        estado = False
        
        if contador > 0:
            fecha_lejana = fechas_declaraciones[0]
            fecha_cercana = fechas_declaraciones[0]
            
            for i in fechas_declaraciones:
                if i < fecha_lejana:
                    fecha_lejana = i
                if i > fecha_cercana:
                    fecha_cercana = i
                    
            edad_minima = edades[0]
            edad_maxima = edades[0]

            for i in edades:
                if i < edad_minima:
                    edad_minima = i
                if i > edad_maxima:
                    edad_maxima = i
                    
            total_edades = 0
            
            for i in edades:
                total_edades += i
                
            monto_minimo = monto_declaraciones[0]
            monto_maximo = monto_declaraciones[0]

            for i in monto_declaraciones:
                if i < monto_minimo:
                    monto_minimo = i
                if i > monto_maximo:
                    monto_maximo = i
                    
            total_montos = 0
            
            for i in monto_declaraciones:
                total_montos += i
            
            print("La cantidad de contribuyentes registrados es:", contador)
            print("La edad más pequeña registrada es:", edad_minima)
            print("La edad más grande registrada es:", edad_maxima)
            print("El promedio de las edades registradas es:", total_edades / contador, "%")
            print("La fecha de declaracion mas cercana es:", fecha_cercana)
            print("La fecha de declaracion mas lejana es:", fecha_lejana)
            print("El monto mas pequeño registrado es:", monto_minimo)
            print("El monto mas grande registrado es:", monto_maximo)
            print("El promedio de los montos registrados es:", total_montos / contador, "%")
            
    
    else:
        print("Por favor ingrese un valor válido")


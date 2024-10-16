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
        #Ingresar obligatoriamente en formato entero ya que no es posible validar que no se ingresen letras
        edad = int(input("Por favor ingrese su edad (ingresar obligatoriamente en formato entero): "))
        fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        profesion = input("Por favor ingrese su profesión: ")
        fecha_declaracion = input("Por favor ingrese la fecha de la declaración (DD/MM/AAAA): ")
        #Ingresar obligatoriamente numeros ya que no es posible validar que no se ingresen letras
        monto_declarar = int(input("Por favor ingrese el monto a declarar (ingresar obligatoriamente numeros): "))
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
            
            print("La cantidad de contribuyentes registrados es:", contador)
            print("La edad más pequeña registrada es:", calcular_edad_minima(edades))
            print("La edad más grande registrada es:", calcular_edad_maxima(edades))
            print("El promedio de las edades registradas es:", calcular_promedio_edades(edades), "%")
            print("La fecha de declaracion mas cercana registrada es:", calcular_fecha_declaraciones_cercana(fechas_declaraciones))
            print("La fecha de declaracion más lejana registrada es:", calcular_fecha_declaraciones_lejana(fechas_declaraciones))
            print("El monto mas pequeño registrado es:", calcular_monto_minimo(monto_declaraciones))
            print("El monto más grande registrado es:", calcular_monto_maximo(monto_declaraciones))
            print("El promedio de los montos registrados es:", calcular_promedio_montos(monto_declaraciones), "%")
            for i in range(contador):
                print("La profesión del contribuyente", i+1, "es:", profesiones[i])
                print("El origen de los fondos del contribuyente", i+1, "es:", origen_fondos[i])
            
    
    else:
        print("Por favor ingrese un valor válido")


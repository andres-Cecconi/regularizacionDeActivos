from funciones import *

print("¡Hola! Estás a punto de comenzar el proceso para regularizar tus activos en Argentina de manera sencilla y transparente. Este programa te ofrece la oportunidad de poner al día tus bienes y cumplir con tus obligaciones fiscales, todo con el respaldo de un sistema claro y accesible.")

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
        Abogado/a
        Médico/a
        Contador/a
        Ingeniero/a (en diversas ramas: civil, industrial, sistemas, etc.)
        Arquitecto/a
        Psicólogo/a
        Enfermero/a
        Licenciado/a en Administración
        Profesor/a
        Diseñador/a Gráfico/a
        Periodista
        Farmacéutico/a
        Veterinario/a
        Técnico/a en Informática
        Trabajador/a Social
        Electricista
        Chef
        Diseñador/a Industrial
        Técnico/a en Construcción
        Sastre/a
        Estilista/Peluquero/a
        Traductor/a
        Técnico/a en Higiene y Seguridad en el Trabajo
        Guía de Turismo
        Músico/a
        Actor/Actriz
        Productor/a de Eventos
        Cocinero/a
        Carpintero/a
        Albañil
        Ingeniero/a en Sistemas
        Fisioterapeuta
        Nutricionista
        Fonoaudiólogo/a
        Oftalmólogo/a
        Odontólogo/a
        Líder de Ventas/Vendedor/a
        Perito/a
        Notario/a
        Coach Personal o Empresarial
        Consultor/a
        Científico/a
        Matemático/a
        Analista de Datos
        Bioquímico/a
        Antropólogo/a
        Técnico/a en Energías Renovables
        Decorador/a de Interiores
        Asesor/a Financiero/a
        Investigador/a
        Programador/a
        Técnico/a en Logística
        Artista Plástico/a
        Cineasta
        Licenciado/a en Relaciones Públicas
        Operador/a de Radio
        Estilista de Moda
        Diseñador/a de Moda
        Maestro/a de Obras
        Técnico/a en Redes y Telecomunicaciones
        Otro
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
        origenes_fondos = """
        Rendimientos de Actividades Comerciales o Profesionales"
        Rendimientos de Inversiones Financieras"
        Ingresos por Actividades en el Exterior"
        Venta de Bienes Inmuebles
        Herencias o Donaciones
        Ahorros o Dinero en Efectivo No Declarado
        Rendimientos de Actividades No Registradas (Trabajo Informal)
        Préstamos o Créditos
        Fondos Derivados de Criptomonedas
        Fondos de Origen Empresarial o Comercial (Sociedades)
        Fondos de Actividades Agrícolas
        """
        print(origenes_fondos)
        origen_fondo = input("Por favor ingrese el origen de los fondos (no se permiten fondos de origen ilícito): ")

        edades.append(edad)
        profesiones.append(profesion)
        fechas_declaraciones.append(fecha_declaracion)
        monto_declaraciones.append(monto_declarar)
        origen_fondos.append(origen_fondo)

    elif contribuyente == "S" or contribuyente == "s":
        print("Has finalizado exitosamente tu trámite de regularización de activos. Gracias por utilizar nuestra plataforma y por cumplir con tus obligaciones fiscales de manera responsable.")
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
                
            # Mostrar el ranking de profesiones (sin ordenar)
            print("\nRanking de Profesiones (Sin ordenar):")
            for profesion, cantidad in profesiones.items():
                print(f"Profesión {profesion}: {cantidad} contribuyentes")
            
            # Mostrar el ranking de orígenes de fondos (sin ordenar)
            print("\nRanking de Orígenes de Fondos (Sin ordenar):")
            for origen, cantidad in profesiones.items():
                print(f"Origen {origen}: {cantidad} contribuyentes")
            
    
    else:
        print("Por favor ingrese un valor válido")


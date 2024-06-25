import os
os.system("cls")

datos=[]

while True:
    print("\nBienvenido a Auto Seguro")
    print("1. Ingresar datos del Vehiculo\n2. Buscar Vehiculo\n3. Imprimir Certificado\n4. Salir")
    try:
        opcion=int(input("Escoja una opción: "))
    except:
        opcion=0
    if opcion<1 or opcion>4:
        print("Opcion invalida")
    elif opcion==1:
        while True:
            try:
                tipo_veh=int(input("¿Qué tipo de vehiculo es?\n1. Automóvil\n2. Camión\n3. Camioneta\n4. Moto\n>"))
            except:
                tipo_veh=0
            if tipo_veh<1 or tipo_veh>4:
                print("Tipo de vehiculo no existe")
            elif tipo_veh==1:
                tipo="Automóvil"
                break
            elif tipo_veh==2:
                tipo="Camión"
                break
            elif tipo_veh==3:
                tipo="Camioneta"
                break
            elif tipo_veh==4:
                tipo="Moto"
                break
        val_patente=""
        while val_patente=="":
            patente=input("Ingrese La patente del vehiculo (xxxx-11): ")
            val_patente=patente.replace(" ","")
            if val_patente=="":
                print("Debe Ingresar una patente")
            elif len(val_patente)!=6:
                print("recuerde que debe tener 4 letras seguidas de 2 numeros")
                val_patente=""
        val_marca=""
        while val_marca=="":
            marca=input("Ingrese la marca del vehiculo: ")
            val_marca=marca.replace(" ","")
            if val_marca=="":
                print("Debe ingresar una marca")
            elif len(val_marca)<3 or len(val_marca)>15:
                print("Ingrese una marca existente")
                val_marca=""
        while True:
            try:
                precio=int(input("Ingrese el valor del vehiculo: "))
            except:
                precio=0
            if precio<5000000:
                print("No aceptamos vehiculos con tan poco valor")
            else:
                break
        while True:
            try:
                tiene_multas=int(input("¿El vehiculo cuenta con multas?\n1. Si\n2. No\n>"))
            except:
                tiene_multas=-1
            if tiene_multas<1 or tiene_multas>2:
                print("opcion invalida")
            elif tiene_multas==1:
                while True:
                    try:
                        monto_multa=int(input("Ingrese el valor de la multa: "))
                    except:
                        monto_multa=0
                    if monto_multa<1:
                        print("el valor de la multa no puede ser 0")
                    fecha_multa=input("Ingrese la fecha de la multa (dd/mm/aa) ")
                    if len(fecha_multa)<=7 or len(fecha_multa)>8:
                        print("recuerda que debe ser 01/01/01")
                        tiene="Si"
                    break
                
            else:
                tiene="No"
                monto_multa=""
                fecha_multa=""
                break
        while True:
            try:
                run=int(input("Ingrese su RUN sin digito verificador (12345678): "))
            except:
                run=0
            if run<7000000 or run>30000000:
                print("RUN no existe")
            else:
                break
        val_nombre=""
        while val_nombre=="":
            nombre=input("Ingrese su nombre: ")
            val_nombre=nombre.replace(" ","")
            if val_nombre=="":
                print("Debe Ingresar un nombre")       
        fecha_registro="24/06/2024"
        
        vehiculo={
            "Vehiculo":tipo,
            "Patente":patente,
            "Marca":marca,
            "Valor":precio,
            "Multas":tiene,
            "Valor Multa":monto_multa,
            "Fecha Multa":fecha_multa,
            "RUN":run,
            "Dueño":nombre,
            "fecha de ingreso":fecha_registro
            }
        
        datos.append(vehiculo)
        print("vehiculo registrado con exito")
    
    elif opcion==2:
        
         while True:
            
             bus_patente=input("Ingrese patente para buscar los datos del vehiculo: ")
             if bus_patente!=patente:
                 print("Patente no existe")
             else:
                bus_patente=(vehiculo for vehiculo in datos if vehiculo["Patente"]==patente)
                print(f'{vehiculo["Vehiculo"]} {vehiculo["Patente"]} {vehiculo["Marca"]} {vehiculo["Valor"]} {vehiculo["Multas"]} {vehiculo["Valor Multa"]} {vehiculo["Fecha Multa"]} {vehiculo["RUN"]} {vehiculo["Dueño"]} {vehiculo["fecha de ingreso"]}')
                break
            
    elif opcion==3:
        while True:
            try:
                vopcion=int(input("¿Qué Certificado desea Imprimir?\n1. Emision de contaminantes\n2. Anotaciones vigentes\n3. Multas\n>"))
            except:
                vopcion=0
            if vopcion<1 or vopcion>3:
                print("Seleccione un certificado")
            elif vopcion==1:
                bus_patente=input("Ingrese patente para buscar los datos del vehiculo: ")
                if bus_patente==patente:
                    patente_vehiculo=[vehiculo for vehiculo in datos if vehiculo["Patente"]==bus_patente]
                    print(f'Emision de Contaminantes: {vehiculo["Patente"]} {vehiculo["Dueño"]} {vehiculo["RUN"]}')
                    break
            elif vopcion==2:
                bus_patente=input("Ingrese patente para buscar los datos del vehiculo: ")
                if bus_patente==patente:
                    patente_vehiculo=[vehiculo for vehiculo in datos if vehiculo["Patente"]==bus_patente]
                    print(f'Anotaciones Vigentes: {vehiculo["Patente"]} {vehiculo["Dueño"]} {vehiculo["RUN"]}')
                    break
            elif vopcion==3:
                bus_patente=input("Ingrese patente para buscar los datos del vehiculo: ")
                if bus_patente==patente:
                    patente_vehiculo=[vehiculo for vehiculo in datos if vehiculo["Patente"]==bus_patente]
                    print(f'Multas: {vehiculo["Patente"]} {vehiculo["Dueño"]} {vehiculo["RUN"]}')
                    break
            
    elif opcion==4:
        print("¡Hasta pronto!")
        break
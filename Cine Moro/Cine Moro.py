niño = 5500
joven = 7000
adulto = 9000
tniño = 0
tjoven = 0
tadulto = 0
cniño = 0
cjoven = 0
cadulto = 0
total = 0
centradas = 0
acum = 0
eacumn = 0
eacumj = 0
eacuma = 0
sw = 1
cate = ""
while sw == 1:
    print("¡Hola! Bienvenido a cine Moro.")
    print()
    print("—————————   Precios Entradas   —————————")
    print("Categoría           Edad          Precio")
    print("(1) Niño        (1 - 13 Años)     $5.500")
    print("(2) Joven      (14 - 21 Años)     $7.000")
    print("(3) Adulto    (Mayor a 22 años)   $9.000")
    print("(6) Registro de ventas + finalizar.")
    try:
        op = int(input("Ingrese el tipo de entrada deseado: "))
        if op == 1:
            cate += " Niño "
            cniño = int(input("Ingrese la cantidad de entradas deseada: "))
            centradas += cniño
            tniño = cniño * niño
            total += tniño
            eacumn += cniño
            salir = int(input("¿Desea continuar?: Si (1) / No (2): "))
            if salir == 2:
                print(f"Categoría: {cate}")
                print(f"Cantidad de entradas: {centradas}")
                print(f"Total a pagar: {total}")
                print("Gracias por su compra: disfrute la función.")
        if op == 2:
            cate += " Joven "
            cjoven = int(input("Ingrese la cantidad de entradas deseadas: "))
            centradas += cjoven
            tjoven = cjoven * joven
            total += tjoven
            eacumj += cjoven
            salir = int(input("¿Desea continuar?: Si (1) / No (2): "))
            if salir == 2:
                print(f"Categoría: {cate}")
                print(f"Cantidad de entradas: {centradas}")
                print(f"Total a pagar: {total}")
                print("Gracias por su compra: disfrute la función.")
        if op == 3:
            cate += " Adulto "
            cadulto = int(input("Ingrese la cantida de entradas deseadas: "))
            centradas += cadulto
            tadulto = cadulto * adulto
            total += tadulto
            eacuma += cadulto
            salir = int(input("¿Desea continuar?: Si (1) / No (2): "))
            if salir == 2:
                print(f"Categoría: {cate}")
                print(f"Cantidad de entradas: {centradas}")
                print(f"Total a pagar: {total}")
                print("Gracias por su compra: disfrute la función.")
        if op == 6:
            acum += total
            print("——— Cantidad de entradas vendidas ———")
            print(f"Niño: {eacumn} — {int((eacumn * 100) / centradas)}%")
            print(f"Joven: {eacumj} — {int((eacumj * 100) / centradas)}%")
            print(f"Adulto: {eacuma} — {int((eacuma * 100) / centradas)}%")
            print(f"Total de entradas: {centradas}")
            print(f"Dinero total recaudado: {acum}")
            sw = 2
    except:
        print("Dato erróneo.")
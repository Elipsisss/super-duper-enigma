import numpy 
import time


list_rut = []
list_fila = []
list_columna = []
p_te = 120000
g_te = 80000
s_te = 50000
contador1 = 0
contador2 = 0
contador3 = 0
total1 = 0
total2= 0
total3 = 0


def ver_menu():
    print("""
        Menú
    1.Comprar entradas
    2.Mostrar ubicacioens disponibles
    3.Ver listado de asistentes
    4.Mostrar ganancias totales
    5.Salir
    """)


def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("Error debe de seleccionar una opción valida")
        except:
            print("ERROR")

def validar_opcion_entrada():
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4):
                return opc
            else:
                print("Error debe de seleccionar una opción valida")
        except:
            print("ERROR")


escenario = numpy.zeros((10,10), int)

def ver_escenario():
    print("     ESCENARIO")
    for x in range (10):
        print(f"FILA: {x+1}", end=" ")
        for y in range (10):
            print(escenario[x][y], end=" ")
        print()
    print("      1 2 3 4 5 6 7 8 9 10")


def cant_entrada():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de entradas a comprar: "))
            if cantidad >= 0 and cantidad <= 3:
                print("registrado")
                return cantidad
            else:
                print("ERROR")
        except:
            print("ERROR")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut: "))
            if len(str(rut)) >= 7  and len(str(rut)) <= 8:
                print("Rut registrado")
                return rut
            else:
                print("RUT NO VALIDO")
        except:
                print("ERROR")

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese la fila en al que desea estar (Premium 1-2) (Gold 3-5) Silver(6-10): "))
            if fila >= 1 and fila <= 10:
                return fila
            else:
                print("fila invalida")
        except:
            print("ERROR")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese la columna en al que desea estar (1-10): "))
            if columna >= 1 and columna <= 10:
                return columna
            else:
                print("fila invalida")
        except:
            print("ERROR")



def entrada():
    if 0 not in escenario:
        print("NO HAY ESPACIO")
        return
    
    ver_escenario()
    menu_entrada()
    cant_entrada()
    
    rut = validar_rut()
        
    fila = validar_fila()
    columna = validar_columna()
    if escenario[fila-1] [columna-1] == 0:
        escenario[fila-1][columna-1] = 1
        list_rut.append(rut)
        list_fila.append(fila)
        list_columna.append(columna)


def menu_entrada():
    while True:
        print(f""" 
        1.Entrada Premium: {p_te}
        2.Entrada Gold: {g_te}
        3.Entrada Silver: {s_te}
        4.Volver al menu principal
        """)
        validar_opcion_entrada()
        return

def cantidad_entrada():
    while True:
        try:
            e_cantidad = int(input("Ingrese cantidad de entradas a comprar: "))
            if e_cantidad >= 1 and e_cantidad <= 3:
                return e_cantidad
            else:
                print("Puede comprar maximo 3 entradas")
        except:
            print("ERROR")



def asistentes():
    print(list_rut)
    

def cont ():
    opc = validar_opcion_entrada
    cant = cant_entrada
    
    if opc == 1:
        total1 = total1 + (cant * p_te)
        contador1 = contador1 + 1
    elif opc == 2:
        total2 = total2 + (cant * g_te)
        contador2 = contador2 + 1
    elif opc == 3:
        contador3 = contador3 + 1 
        total3 = total3 + (cant * s_te)
    print (f"""
    Tipo entrada / Cantidad / Total
    Platinum /   ${contador1} / ${total1} 
    Gold    / ${contador2} / ${total2} 
    Silver / ${contador3} / ${total3}
    
    """)
    return
    

     

    
    
   


        















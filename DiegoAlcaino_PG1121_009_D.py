
import funciones as fn
import time
contador1 = 0
contador2 = 0
contador3 = 0
total1 = 0
total2= 0
total3 = 0
p_te = 120000
g_te = 80000
s_te = 50000

while True:
    fn.ver_menu()
    opc = fn.validar_opcion()
    if opc == 1:
        fn.entrada()
        
    elif opc == 2:
        fn.ver_escenario()
    elif opc == 3:
        fn.asistentes()
    elif opc == 4:
        fn.cont()
    elif opc == 5:
        fn.ver_escenario()
    else:
        print("GRACIAS POR PREFERIRNOS")
        print("06/07/2023")
        break


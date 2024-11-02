import calendar

def inicio():

    yy = 2012
    mm = 12

    print(calendar.month(yy, mm))
    #Este fue el primer código que funcionó con esta librería

opc = ''

while(True):
    start = int(input("Digite 1 si quiee el calendario completo por año, 2 si quiere elegir el año y el mes: "))
    if start == 1:
        year=int(input("Digite el año del cual quiere el calendario: "))

        for i in range (1, 13):
            print(calendar.month(year, i))
    
    elif start == 2:
        año = int(input("Digite el año: "))
        mes = input("Escriba el mes empezando con mayúscula: ")
        if mes == 'Enero':
            mes = 1
        elif mes == 'Febrero':
            mes = 2
        elif mes == 'Marzo':
            mes = 3
        elif mes == 'Abril':
            mes = 4
        elif mes == 'Mayo':
            mes = 5
        elif mes == 'Junio':
            mes = 6
        elif mes == 'Julio':
            mes = 7
        elif mes == 'Agosto':
            mes = 8
        elif mes == 'Septiembre':
            mes = 9
        elif mes == 'Octubre':
            mes = 10
        elif mes == 'Noviembre':
            mes = 11
        elif mes == 'Diciembre':
            mes = 12
        print(calendar.month(año, mes))

    opc = input("Digite 'Salir' si es su desición, caso contrario digite 'No salir' ")
    if opc == 'Salir':
        break;
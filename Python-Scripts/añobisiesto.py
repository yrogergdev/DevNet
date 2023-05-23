year = int(input ("Ingrese el numero de año: "))
if year >= 1582:
    print("Año dentro de la era Gregoriana")
    if 0 != (year % 4):
        print(year, "Año comun")
    elif  0 != year % 100:
        print(year, "Año Bisiesto")
    elif 0 != year % 400:
        print(year, "Año comun")
    else :
        print(year, "Año Bisiesto" )
else:
    print("No esta dentro del periodo del calendario Gregoriano")
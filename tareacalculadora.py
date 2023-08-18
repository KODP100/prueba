numer1 = int(input("Ingrese un numero: "))
numer2 = int(input("Ingrese otro numero: "))

eleccion = 0

while eleccion != 6:
    print(""" 
    seleccione una opcion 
    
    1) suma
    2) resta
    3) multiplicacion
    4) division
    5) cambiar numero de operacion
    6) salir
    """)

    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("resultado: ", numer1,"+", numer2,"=", numer1+numer2)

    if eleccion == 2:
        print(" ")
        print("resultado: ", numer1,"-", numer2,"=", numer1-numer2)
    
    if eleccion == 3:
        print(" ")
        print("resultado: ", numer1,"*", numer2,"=", numer1*numer2)

    if eleccion == 4:
        print(" ")
        print("resultado: ", numer1,"/", numer2,"=", numer1/numer2)

    if eleccion == 5:
        numer1 = int(input("Ingrese un numero: "))
        numer2 = int(input("Ingrese otro numero: "))

    if eleccion == 6:
        print("vuelve pronto, atetamente su servilleta")
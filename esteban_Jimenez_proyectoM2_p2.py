##################################################### proyecto #2   ###############


x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

# Verificar que ninguna coordenada sea igual a 0
if x == 0 or y == 0:
    print("Ninguna coordenada puede ser igual a 0.")
else:
    if x > 0:
        if y > 0:
            print("El punto se encuentra en el cuadrante I.")
        else:
            print("El punto se encuentra en el cuadrante IV.")
    else:
        if y > 0:
            print("El punto se encuentra en el cuadrante II.")
        else:
            print("El punto se encuentra en el cuadrante III.")
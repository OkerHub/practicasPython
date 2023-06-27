nombre = input("introduce tu nombre: ")

apellidoPaterno= input("introduce tu apellido Paterno: ")

apellidoMaterno = input("introduce tu apellido Materno: ")

masa = float(input("introduce tu masa en kilogramos: "))

estatura = float(input("introduce tu estatura en metros: "))

imc=masa/estatura**2

print("Nombre" + nombre)
print("Apellido Paterno" + apellidoPaterno)
print("Apellido Materno" + apellidoMaterno)
print("peso " + str(masa))
print("estatura" + str(estatura))
print("Tu indice de masa corporal es de: " + str(imc))
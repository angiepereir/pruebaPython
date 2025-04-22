##declarar variables##
#nombre = input("cual es tu nombre? ")
edad = int(input("¿cual es tu edad? "))
#print(f"hola {nombre}! tienes {edad} años")

#def saludar(nombre):
   # print(f"Hola, {nombre}, bienvenido al taller ")
#saludar(nombre)

#for recorrer in range (1, 10):
    #print(recorrer)

def esMayorDeEdad(edad):
    if edad >=18:
        return "eres mayor de edad"
    else:
        return "eres menor de edad"
print (esMayorDeEdad(edad))
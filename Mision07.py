#Irma Gómez Carmona, A01747743
#Menú con ciclos while para ejecutar las opciones

def seleccionarOpcion():
    print("")
    print("Misión 07. Ciclos While")
    print("Autor: Irma Gómez Carmona ")
    print("Matrícula: A01747743")
    print("1. Calcular divisiones")  # opciones
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcionM = int(input("Teclea tu opción:"))
    print("")
    return opcionM


def dividir( dividendo, divisor):
    contador=0   #resultado (el número de veces que el dividor se le puede restar exactamente al dividendo)
    D1=dividendo
    D2=divisor
    while D1>=D2: #mientras que el dividendo siga siendo mayor que el divisor se ejecuta el ciclo
        D1-=D2
        contador+=1
    print("%d / %d = %d , sobra %d" % (dividendo,divisor,contador,D1))


def encontrarMayor(num1, num2): #se comparan los dos números para encontrar el mayor
    if num1>num2:
        return num1
    return num2


def main():
    opcionM=seleccionarOpcion()
    while opcionM!=3: #mientras que la opciones sean diferentes a 3 se ejecutará el menú
        if opcionM==1:
            dividendo=int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo,divisor)

        elif opcionM==2:
            num2 = 0
            cont=0
            num1 = int(input("Teclea un número [-1 para salir]: "))
            if num1==-1:
                print("No hay valor mayor")
            else:
                while num1 !=-1:
                    num2 = encontrarMayor(num1, num2)
                    num1 = int(input("Teclea un número [-1 para salir]: "))
                print("El mayor es: ", num2)

        elif opcionM!=3:
            print("ERROR, teclea 1, 2 o 3")  #si no se cumplen las demás condiciones, es un valor invalido

        opcionM = seleccionarOpcion()

    print("Gracias por usar este programa, regrese pronto") #se termina el programa

main ()

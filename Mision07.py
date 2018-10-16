#Irma Gómez Carmona, A01747743
#Menú con ciclos while para ejecutar las opciones


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
    opcionM=1
    while opcionM!=3: #mientras que la opciones sean diferentes a 3 se ejecutará el menú
        print("")
        print("Misión 07. Ciclos While")
        print("Autor: Irma Gómez Carmona ")
        print("Matrícula: A01747743")
        print("1. Calcular divisiones")   #opciones
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcionM=int(input("Teclea tu opción:"))
        print("")

        if opcionM==1:
            dividendo=int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo,divisor)

        elif opcionM==2:
            num1 = 0
            num2 = 0
            cont=0
            while num1 !=-1:
                num1 = int(input("Teclea un número [-1 para salir]: "))
                num2 = encontrarMayor(num1, num2)
                cont+=1
            if cont>1:   #si el ciclo se ejecuta más de una vez se imprime el número mayor del  conjunto
                print("El mayor es: ", num2)
            else:
                print("No hay valor mayor") #de lo contrario, se imprime que no hay valor mayor

        elif opcionM!=3:
            print("ERROR, teclea 1, 2 o 3")  #si no se cumplen las demás condiciones, es un valor invalido

    print("Gracias por usar este programa, regrese pronto") #se termina el programa

main ()
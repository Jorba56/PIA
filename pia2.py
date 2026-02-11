opcion=input("1.- Nombre completo\n 2.-Calculadora\nIngrese una opción: ")
if opcion=="1":
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    ano_nacimiento=int(input("Ingrese su año de nacimiento: "))
    print("Hola", nombre, apellido, "tu edad es:", 2026-ano_nacimiento)
elif opcion=="2":
    num1=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese el segundo número: "))
    operacion=input("Ingrese la operación (+, -, *, /): ")
    if operacion=="+":
        print("El resultado es:", num1+num2)
    elif operacion=="-":
        print("El resultado es:", num1-num2)
    elif operacion=="*":
        print("El resultado es:", num1*num2)
    elif operacion=="/":
        if num2!=0:
            print("El resultado es:", num1/num2)
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operación no válida.")


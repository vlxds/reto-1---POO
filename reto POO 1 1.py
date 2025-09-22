n1 = float(input("ingresa el primer numero: "))
n2 = float(input("ingresa el segundo numero: "))
operacion = input("ingresa el simbolo de la operación: ")
r:float = 0.0

if operacion == "+":
    r = n1 + n2
    print("resultado: ", r)
elif operacion == "-":
    r = n1 - n2
    print("resultado: ", r)
elif operacion == "*":
    r = n1 * n2
    print("resultado: ", r)
elif operacion == "/":
    r = n1 / n2
    print("resultado: ", r)
else:
    print("ERROR! :( ")
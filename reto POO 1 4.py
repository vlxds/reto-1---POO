n = int(input("¿cuántos números deseas ingresar?: "))
numeros = []
y=0

for i in range(n):
    r = int(input("ingresa numero: "))
    numeros.append(r)

for j in range(n-1):
    x = numeros[j] + numeros[j+1] #realiza la suma de los numeros consecutivos
    print(x)
    if x > y: # compara si la suma actual es mayor a la anterior
        y = x

print("El resultado de la suma de numeros consecutivos mas grade de la lista es: ", y)
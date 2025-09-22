n = int(input("¿cuántos números deseas ingresar?: "))
numeros = []
primos = []

for i in range(n):
    r = int(input("ingresa numero: "))
    numeros.append(r)

#revisa si la división con todos los numeros naturales menores o guales a el tienen residuo iguala a cero
for j in numeros:
    w = 0
    for k in range(j):
        s = j % (k+1)
        if s == 0:
            w += 1
    if w == 2:
        primos.append(j)

print(primos)

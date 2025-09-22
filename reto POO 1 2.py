palabra = input("ingresar palabra: ")

m = len(palabra)
n = int(m/2)
o = 0
p = m -1
s = False

#convierte la palabra en una lista y compara la primera letra con la ultima y se van corriendo hacia el centro
for i in range(n):
    if palabra[o] == palabra[p]:
        o += 1
        p -= 1
    else :
        s = True

print(n)
if s:
    print("la palabra ", palabra, "no es un palíndromo")
else:
    print("la palabra ", palabra, "es un palíndromo")

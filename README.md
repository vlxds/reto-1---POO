# reto-1---POO

## Punto 1.
El programa solicita al usuario 3 elementos, 2 numeros enteros y el simbolo de la operación matematica que quiere realizar. Luego revisa cual fue el simbolo de la operación matematica que se ingreso y ejecuta la operación con los dos numeros ingresados y al final imprime el resultado.
```python
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
```

## Punto 2.
El programa solicita al usuario una palabra. Luego convierte la palabra en una lista y se revisa si la primera letra es igual a la ultima, luego se van conrriendo la posición hacia el interior e itera el proceso. Si en algun punto, las letras no coinciden, hara que un variable tipo booleano sea falso e imprima el mensaje "la palabra no es un palíndromo", de lo contrario la variable sera verdadera e imprimirá  "la palabra no es un palíndromo".

```python
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
```

## Punto 3.

El programa solicitara al usuario la cantidad de números que desea ingresar y los respectivos numeros enteros, los cuales van a ser almacenados en una lista. Luego se va a seleccionar uno por uno los numeros de la lista, se les divide por todos los numeros naturales (sin contar el 0) menores e iguales a él y se revisa el residuo, si este valor es igual a cero, se suma 1 a un contador, cuando acaba de hacer todas las divisiones que debe realizar, se revisa el numero del contador, si este es igual a 2, ingresa el numero a una lista donde se guarda los numeros que son primos. Este proceso se itera para los demas numeros de la lista y al final se imprime la lista con todos los numeros primos que habian en la lista ingresada por el usuario, si hubo alguno, de lo contrario imprimira una lista vacia.  

``` python
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
```

## Punto 4.
El programa solicitara al usuario la cantidad de números que desea ingresar y los respectivos numeros enteros, los cuales van a ser almacenados en una lista. Luego se va a seleccionar el primer numero de la lista y el consecutivo y se suman, luego se compara si este resultado es mayor al resultado anterior (como es primero, este se compara con el 0) y se actualiza la variable que va contener la suma mas grande. Este proceso se itera con el resto de numeros de la lista y al final se imprime el resultado.

```python
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
```

## Punto 5.
El programa solicitará al usuario una cantidad de palabras, que van a ser ingresadas a una lista hasta que el usuario ingrese a letra "f" el cual finaliza el proceso de solicitud de palabras. Luego se selecciona la primera palabra de la lista y se ordenan las letras en orden alfabetico en una lista, ignorando las letras repetidas, y se ingresan en otra lista. Este proceso se itera con el resto de las palabras. A continuación, se comparan las palabras ordenadas alfabeticamente y si coinciden, de la lista con las palabras no modificadas se van agregando a una lista y se van retirando las palabras ordenadas para que no se repitar. Este proceso se itera con las demas palabras y al final se imprime una lista con todas las palabras que coincidian, si es que las hay.

```python
import string #libreria con unas constantes interesantes y muy utiles

n: str = "uwu"
palabras: list = []
resultado: list = []
final:list = []

while n != "f":
    n = str(input("Ingresa la palabra o ingresa f para finalizar: "))
    if n != "f":
        palabras.append(n)

caracteres = []
m_caracteres = []

#ordenar cada palabra en orden alfabetico, ignorando las letras repetidas
for i in palabras:
    pl = list(i) #convierte una palabra seleccionada en una lista
    abc = list(string.ascii_lowercase)
    for j in abc: # selecciona una letra del abecedario en orden alfabetico
        c: bool = False
        for k in pl: #selecciona una letra de la palabra
            if j == k: #compara la letra seleccionada de la palabra con la letra seleccionada del abecedario
                c = True
        if c: #si la letra de la palabra coincide con la letra del abecedario, esta sera agregada a una lista
            caracteres.append(j)
    m_caracteres.append(caracteres)
    caracteres = [] #arreglo con las palabras en forma de lista y con las letras ordenadas alfabeticamente


#revisa si las palabras son iguales y las guarda en un arreglo
for p in range(len(m_caracteres)-1):
    aa = m_caracteres[p]
    cc: bool = False
    for q in range((p+1),len(m_caracteres)):
        bb = m_caracteres[q]
        if aa != "@" and aa == bb: #revisa si las palabras son iguales
            cc = True
            resultado.append(palabras[q])
            m_caracteres[q] = "@"
    if cc:
        resultado.insert(0,palabras[p])
        final.append(resultado)
    resultado = []

print(final)
```

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
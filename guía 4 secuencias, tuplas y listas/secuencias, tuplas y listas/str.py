# Métodos de la clase str (String)
# capitalize() # -> Devuelve el string con la primera letra en mayúscula. -> "hola".capitalize()
# center(ancho[,relleno]) # -> Devuelve el string centrado con relleno a los costados. -> "Python".center(10, "*")
# count(valor) # -> Devuelve la cantidad de veces que aparece "valor" en el string. -> "banana".count("a")
# count(valor) # -> Devuelve la cantidad de veces que aparece "valor" en el string. -> # ->
# find(substring[,desde[,hasta]]) # -> Devuelve la primera posición de comienzo del substring en el string. -> "python".find("th")
# rfind(substring[,desde[,hasta]]) # -> Devuelve la última posición de comienzo del substring en el string. -> "python programming".rfind("ing")
# format(args,*) # -> Devuelve el string formateado con valores sustituidos. -> "Mi nombre es {} y tengo {} años".format("Juan", 25)
# upper() # -> Devuelve el string en mayúsculas. -> "hola".upper()
# lower() # -> Devuelve el string en minúsculas. -> "Hola".lower()
# strip() # -> Devuelve el string sin espacios en blanco al inicio y al final. -> " Python ".strip()
# replace(viejo, nuevo) # -> Devuelve el string con todas las apariciones de "viejo" reemplazadas por "nuevo". -> "Hello, World!".replace("Hello", "Hi")
# split([separador]) # -> Devuelve una lista de substrings separados por "separador". -> "apple,banana,grape".split(",")
# join(iterable) # -> Devuelve un string que es la concatenación de los elementos en el iterable. -> ",".join(["apple", "banana", "grape"])
# isdigit() # -> Devuelve True si todos los caracteres son dígitos. -> "12345".isdigit()
# isalpha() # -> Devuelve True si todos los caracteres son letras. -> "Python".isalpha()
# startswith(substring) # -> Devuelve True si el string comienza con "substring". -> "Hello, World!".startswith("Hello")
# rindex(substring[,desde[,hasta]]) # -> Devuelve la última posición de comienzo del substring en el string. -> "python programming".rindex("ing")
# join(iterable) # -> Devuelve un string que es la concatenación de los elementos en el iterable, intercalados con el string. -> ",".join(["apple", "banana", "grape"])
# ljust(ancho[,relleno]) # -> Justifica el string hacia la izquierda con relleno. -> "Python".ljust(10, "-")
# rjust(ancho[,relleno]) # -> Justifica el string hacia la derecha con relleno. -> "Python".rjust(10, "-")
# lower() # -> Devuelve el string en minúsculas. -> "Hola".lower()
# upper() # -> Devuelve el string en mayúsculas. -> "hola".upper()
# maketrans(x[,y[,z]]) # -> Asocia en un diccionario los correspondientes caracteres de las cadenas x e y. -> str.maketrans("aeiou", "12345")
# translate(pares) # -> Devuelve el string con los caracteres asociados en el diccionario pares reemplazados. -> "hello".translate(str.maketrans("aeiou","12345"))"

texto="Bienvenido a mi aplicación{0}"
print(texto.format(" en Python")) 

texto="Bruto: ${bruto} + IVA: ${iva} = Neto: ${neto}"
print(texto.format(bruto=100,iva=21,neto=121)) 

tup=('a','b','c')
print('-'.join(tup)) 

vocales="aeiou"
numeros="12345"
texto="murcielagos"
print(texto.maketrans(vocales,numeros))

vocales="aeiou"
acentos="áéíóú"
texto="murcielagos"
parejas=texto.maketrans(vocales,acentos)
print(parejas)
print(texto.translate(parejas))
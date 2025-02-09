# 8. Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
#
# a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se
# encuentra.
# 
# b. Guardar las tuplas en una lista.
# 
# c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país
# con el siguiente formato:
# País: <nombre>
# Capital: <capital>
# Continente: <continente>
# Por ejemplo:
# País: Japón
# Capital: Tokio
# Continente: Asia

# Recibe un parámetro e imprime la info de cada país
def imprimir_info_paises(paises):
     for i in paises:
          nombre= print(f'País: {i[0]}')
          capital= print(f'Capital: {i[1]}')
          continente= print(f'Continente: {i[2]}')
     return nombre, capital, continente

paises_tupla= (('Francia', 'París', 'Europa'),('Argentina', 'Buenos Aires', 'América del sur'),('Japón', 'Tokyo', 'Asia'),('Alemania', 'Berlín', 'Europa'),('Perú', 'Lima', 'América del Sur'))

paises_lista=list(paises_tupla)

info= imprimir_info_paises(paises_lista)
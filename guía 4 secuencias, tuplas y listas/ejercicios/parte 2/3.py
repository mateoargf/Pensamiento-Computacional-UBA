# 3. Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al segundo, se pide devolver el string habiendo eliminado el substring del mismo.
# Ejemplo:
# string: “Campeones del Mundo - 2022”
# substring: “2022”
# Una vez llamada a la función el string nos debería quedar “Campeones del Mundo - ”, notar que solo borra el año, el espacio no

# Recibe dos parámetrso tipo str(str, substr), devuelve solo el str
def eliminar_substring(texto, subtexto):
     subtexto = subtexto.capitalize()
     if not (subtexto in texto):
          return texto
     else: return texto.replace(subtexto, '')
     
frase = 'Pensamiento Computacional - 2025'
palabra = 'computacional'

print(f'String: {frase} - Substring: {palabra}.')

respuesta = eliminar_substring(frase,palabra)
print(f'String: {respuesta}.')

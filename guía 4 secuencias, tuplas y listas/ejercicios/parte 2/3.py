# 3. Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al segundo, se pide devolver el string habiendo eliminado el substring del mismo.
# Ejemplo:
# string: “Campeones del Mundo - 2022”
# substring: “2022”
# Una vez llamada a la función el string nos debería quedar “Campeones del Mundo - ”, notar que solo borra el año, el espacio no

# Recibe dos parámetrso tipo str(str, substr), devuelve solo el str
def devolver_string(texto, subtexto):
     subtexto = ''
     return texto.format(sub= subtexto)
     
texto_principal = 'Campeones del Mundo - {sub}'
sub_texto = '2022'

print(f'String: {texto_principal.format(sub=sub_texto)} - Substring: {sub_texto}')

respuesta = devolver_string(texto_principal,sub_texto)
print(f'String: {respuesta}.')

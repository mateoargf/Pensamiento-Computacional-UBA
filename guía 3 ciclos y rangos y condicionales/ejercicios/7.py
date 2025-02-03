# 7. Se tienen letras para representar las estaciones del año:
# ● V para verano
# ● O para otoño
# ● I para invierno
# ● P para primavera
# Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
# decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
# ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
# B, V e I.

# Recibe un parámetro y devuelve la estación correspondiente
def devolver_estacion(valor):
     if valor == 'V':
          return 'Verano'
     elif valor == 'O':
          return 'Otoño'
     elif valor == 'I':
          return 'Invierno'
     elif valor == 'P':
          return 'Primavera'
     return 'error'

print('Ingrese un caracter para devolver una estación del año')

usuario = input('Ingrese "V" para verano, "O" para otoño, "I" para invierno y "P" para primavera: ')

respuesta = devolver_estacion(usuario)

print(f'La estación es: {respuesta}')
# print('Ingrese la edad de Juan')
# edad = input()
# print('La edad de Juan es: ', edad)

# operación de asignación
#  se pone a la etiqueta de la izquierda del igual a apuntar al valor resultante de evaluar la expresión de la derecha
# ¡La operación asignación no es conmutativa! Siempre se escribe el nombre de la variable a la izquierda del
# igual y la expresión que producirá el valor resultante a la derecha.

# edad = input('Ingrese la edad de Juan: ')
# print('La edad de Juan es: ', edad)

# print('Quién?')
# nombre = input()
# edad = input(f'Ingrese la edad de {nombre}: ')
# print(f'La edad de {nombre} es {edad}')

# cadena de formateo: print o input(f('texto constante {variable}'))

dia_semana = 'miércoles'
dia_mes = 8
print(dia_semana)# -> Esto nos imprime: "Miércoles"
print(dia_mes) # -> Esto nos imprime: 8

#  usando +:
print('El día de la semana es: ' + dia_semana)
print('El día del mes es: ' + str(dia_mes))

# usando comas:
print('El día de la semana es: ', dia_semana)
print('El día del mes es: ', str(dia_mes))

# usando f''
print(f'El día de la semana es: {dia_semana}')
print(f'El día del mes es: {str(dia_mes)}')

# queremos calcular la edad del hermano mayor
nombre_menor = input('quién es el hermano menor? ')
# casteamos el valor ingresado en int para poder operar
edad_menor = int(input(f'Ingrese la edad de {nombre_menor} ')) 
nombre_mayor = input(f'Cómo se llama el hermano mayor de {nombre_menor}? ')
# otro casteo para transformar el objeto tipo str en int
difer = int(input(f'Cúantos años más tiene de diferencia {nombre_mayor}? '))
# acá operamos los datos casteados
edad_mayor = edad_menor + difer
print(f'{nombre_menor} tiene: {edad_menor} años')
print(f'{nombre_mayor} tiene: {edad_mayor} años')


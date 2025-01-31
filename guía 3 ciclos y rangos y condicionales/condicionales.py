# Operadores lógicos:
# Sin modificar precedencias
# valor1 = True or False and False
# valor2 = True or False or False
# valor3 = True and True and False

# Modificando precedencias
# valor1_modificado = (True or False) and False #sin modificación de precedencias el resultado es verdadero
# valor2_modificado = True or (False or False) #no cambia
# valor3_modificado = True and (True and False) #no cambia

# print(f'los valores sin precedencias "()": valor1: {valor1}, valor 2: {valor2}, valor 3: {valor3}')
# print(f'los valores modificados con precedencias "()": valor1: {valor1_modificado}, valor 2: {valor2_modificado}, valor 3: {valor3_modificado}')

# Ejemplo de cálculo de pago por horas
cant_horas = int(input('Ingrese la cantidad de horas trabajadas: '))
valor_hora = float(input('Ingrese valor de la hora de trabajo: '))
hijos = input('Tiene hijos? (si/no): ')
total = cant_horas * valor_hora
if hijos=='si':
          plus_fijo=float(input('Ingrese adicional guardería: '))
          total = total + plus_fijo
else:
     if (cant_horas >= 30):
          total = total*1.1
print('Debe cobrar', total)

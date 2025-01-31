# hay_sol = False
# hace_frio = True
# if hay_sol and not hace_frio:
#      print('voy a usar gorra y no me pongo buzo')
# elif hay_sol and hace_frio:
#      print('voy a usar gorra y me pongo buzo')
# elif not hay_sol and not hace_frio:
#      print('salgo sin gorra y sin buzo')
# else:
#      print('Salgo sin gorra y me pongo buzo')

# Recibe dos parámetros y hace la división
def division(dividendo, divisor):
     if divisor == 0:
          return 'Error'
     
     return  dividendo / divisor 

print('Ingrese los enteros para la división')

dividendo = float(input(f'Ingrese el dividendo: '))
divisor = float(input(f'Ingrese el divisor: '))

resultado = division(dividendo, divisor)

print(resultado)
# 6. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
# ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
# ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
# Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
# usuario, y no solo para 100?

# Recibe dor parámetros y determina si es menor a un 100 y cuanto falta para llegar
def evaluar_enteros(a, b, limite):
     sum = a + b
     if sum < limite:
          restante = limite - sum
          return(f'falta {restante} para llegar a {limite}')
     return(f'Llega a {limite}')

print('Ingrese dos enteros')

entero_1 = int(input('Ingrese el entero: '))
entero_2 = int(input('Ingrese el entero: '))

limite = int(input(f'Ingrese el límite entero: '))

respuesta = evaluar_enteros(entero_1, entero_2, limite)

print(respuesta)
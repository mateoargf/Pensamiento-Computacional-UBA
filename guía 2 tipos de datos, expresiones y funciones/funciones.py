def imprimir_saludo(nombre):
     print(f'Hola {nombre}!')
nombre = 'Lucas'
imprimir_saludo(nombre)

def obtener_saludo(nombre):
     return f'hola {nombre}!'
nombre = 'Santiago'
saludo = obtener_saludo(nombre) # -> Esto es lo importante, antes no se asignaba ningún valor, ahora que retorna algo, sí

print(saludo)

#Cálculo de operación aritmética binaria
# print('Cálculo de la operación')
# num1 = input('Num 1: ')
# num2 = input('Num 2: ')
# op = input('Operador (+ - * / // %): ')
# result = eval(num1 + op + num2)
# print(f'{num1} {op} {num2} = {result}')

# def calculo(n1,n2,op):
#      return eval(n1+op+n2)
#Cálculo de operación aritmética binaria
# print('Cálculo de operación')
# num1= input('Num 1: ')
# num2 = input('Num 2: ')
# op = input('Operador (+ - * / // % ): ')
# result = calculo(num1, num2, op)
# print(num1,op,num2,'=',result,sep='')

# Función Definición Ejemplo de Uso

print() #Imprime un mensaje o valor en la consola print("Hello, world!")
input() #Lee una entrada de texto desde el usuario name = input("Enter your name: ")
abs() #Devuelve el valor absoluto de un número abs(-5)
round() #Redondea un número al entero más cercano round(3.7)

# Sentencias básicas y datos simples APUNTE DE CÁTEDRA

int() #Convierte un valor en un entero x = int("5")
float() #Convierte un valor en un número de punto flotante y = float("3.14")
str() #Convierte un valor en una cadena de texto message = str(42)
bool() #Convierte un valor en un booleano is_valid = bool(1)
len() #Devuelve la longitud (número de elementos) de un objeto length = len("Hello")
max() #Devuelve el valor máximo entre varios elementos o una secuencia max(4, 9, 2)
min() #Devuelve el valor mínimo entre varios elementos o una secuencia min(4, 9, 2)
pow() #Calcula la potencia de un número result = pow(2, 3)
range() #Genera una secuencia de números numbers = range(1, 5)
type() #Devuelve el tipo de un objeto data_type = type("Hello")
round() #Redondea un número a un número de decimales específico rounded_num = round(3.14159, 2)
isinstance() #Verifica si un objeto es una instancia de una clase específica is_instance = isinstance(5, int)
replace() #Reemplaza todas las apariciones de un substring por otro text = "Hello, World!" new_text = text.replace("Hello", "Hi")

# Recibe el nombre de una persona y la saluda
# def saludar(name):
#      print(f'Hola {name}! Espero que estés muy bien :)')   
       
# saludar('Mateo')
# saludar('Juan')
# saludar('María')
# saludar('Manuel')

# Recibe dos números e imprime la suma por pantalla
# def mostar_suma(sum1, sum2):
#      suma = sum1 + sum2
#      print(f'La suma es = {suma}')
     
# mostar_suma(13,3)

# Recibe 2 números y devuelve la suma de ellos
# def suma(sum1, sum2):
#      res = sum1 + sum2
#      return res

# resu_suma = suma(5, 9)
# print(resu_suma)

# resu_suma = suma(8, 7)
# print(resu_suma)

# Recibe dos números y devuelve la suma y la resta
def resultados(num1, num2):
     sum = num1 + num2
     rest = num1 - num2
     return sum, rest

suma, resta = resultados(18, 30)
print(f'La suma es: {suma}, la resta es: {resta}')

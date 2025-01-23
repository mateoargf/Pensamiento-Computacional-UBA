# Tipo de dato Ejemplos de constantes
# entero – int 9 -5 37 0
# real - float 0.01 88.72156333 -12.0 0.0
# complejo - complex (10,9j) la componente con j del par indica la parte imaginaria
# lógico - bool True False (verdadero y falso)
# texto - str 'Ana y sus HERMANAS!, 7 en total' 'APRENDO A programar ****' 'u' ''

# Operadores
# Símbolo Definición Ejemplo
# + Suma 10+cant
# - Resta saldo-pago
# * Producto a*20
# / División con Precisión Decimal a/3.5
# // División Entera a//12
# % Resto de División num_par%2
# += Suma abreviada, agrega a=a+3 ≈ a+=3
# -= Resta abreviada, quita a=a-3 ≈ a-=3
# *= Producto abreviado a=a*3 ≈ a*=3
# /= División abreviada a=a/3 ≈ a/=3
# //= División entera abreviada a=a//3 ≈ a//=3
# %= Resto de División abreviado a=a%3 ≈ a%=3

cant = 10

print('probamos la suma:', cant + 10)

saldo = 3500
pago = 1200
print('TOTAL de saldo tras el pago:', saldo - pago)

a = 10
print('a*20:', a * 20)
print('a(3.5:', a / 3.5)
print('a//12:', a // 12)

num_par = 7
print('num_par%2:', num_par % 2)

a = a + 3
print(
    'suma + a:',
    a,
    'resta - a:',
    a - 3,
    'producto * a:',
    a * 3,
    'división / a:',
    a / 3,
    'división entera // a:',
    a // 3,
    'resto de división % a:',
    a % 3,
)

print(
    'suma abreviada a+=3:',
    a + 3,
    'resta abreviada a-=3:',
    a - 3,
    'producto abreviado a*=3:',
    a * 3,
    'división abreviada a/=3:',
    a / 3,
    'division entera abreviada a//=3:',
    a // 3,
    'resto de división abreviado a%=3:',
    a % 3,
)
# El orden de prioridad de ejecución va a ser:
# 1. paréntesis ()
# 2. *, / , // , %
# 3. +, -

# Operadores de edición de texto válidos:
# Símbolo Definición Ejemplo
# + Concatenación 'hola'+' juan'-> hola Juan
# * Repetición de Texto 'ja'*3 -> jajaja
# [k] o [-k] Selección de caracter a='hola' a[0] -> h
# a[2] -> l
# [ i : j : p] Selección de una porción del texto. Siendo:
# i : inicio, j : final, p : pasos
# a[0:2]-> ho
# += Concatenación abreviada a = hola
# a+='y chau' -> holay chau
# *= Repetición abreviada a*=2 -> holahola
# Para alterar cualquier precedencia debemos usar (), como en matemáticas
# El orden de prioridad de ejecución va a ser:
# 4. paréntesis ()
# 5. corchetes []
# 6. +, *

print('hola' + ' juan')
print('ja' * 3)

a = 'hola'
print(a[0], a[2], ' ', a)
print(a[0:2])
a *= 2
print(a)
a += ' y chau'
print(a)

# El orden de prioridad de ejecución va a ser:
# 4. paréntesis ()
# 5. corchetes []
# 6. +, *

palabra = 'hola'
print(palabra[2])

palabra = 'pensamiento'
print(palabra[1:3])
print(palabra[3:7])
print(palabra[:3])
print(palabra[3:])
print(palabra[0:10:2])
print(palabra[::3])

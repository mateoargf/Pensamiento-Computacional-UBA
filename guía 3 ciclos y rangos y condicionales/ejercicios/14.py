# 14. Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
# ingresado.
# AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver
# si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea
# distinto de 0, o sea que no sea divisible.

# Recibe un parámetro e imprime los números primos entre 0 y el correspondiente
def es_primo(n): 
     if n < 2:
          return False            
     for i in range(2, n) :
          if n % i == 0:
               return False
     return True
       
def devolver_primos(n):
     for i in range(n + 1):
          if es_primo(i):
               print(f'{i} es primo')                      
          
valor = abs(int(input('Ingrese un entero: ')))

devolver_primos(valor)
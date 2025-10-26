# 2. En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
# cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
# es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
# a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
# b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
# cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta forma:
# Agus
# Manu
# Santi
# Lorena
# Maria
# La función tiene que devolver 5000
# c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
# de los nombres, se agregue también a Tomi.

personas = open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\ejercicios\\regalo.txt', encoding='utf-8')
lista = personas.readlines()
for i in lista:
   i.strip('\n')
   print(i) 
personas.close()

personas = open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\ejercicios\\regalo.txt', encoding='utf-8')
lista = personas.readlines()
def calcular_total(nombres):
   count = 0
   aporte = 1000

   for i in nombres:
      if i.strip('\n') == 'Santi':
         sumar = open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\ejercicios\\regalo.txt', 'a' ,encoding='utf-8')
         sumar.writelines('\nTomi')
         count +=1
      count +=1
   total = count *  aporte  
   return total
   
valor = calcular_total(lista)
print(f'El monto del regalo es de {valor}$')

personas.close()
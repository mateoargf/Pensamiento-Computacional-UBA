texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "r")
texto.close()


texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "w")
texto.write('hola')
texto.write('chau')
texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "w")
texto.writelines(['hola', 'adios'])
texto.writelines('chau')
texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "a")
texto.writelines(['\nhola', 'adios'])
texto.writelines('chau')
texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "r+")
lineas = texto.readlines()
print(lineas)
texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "r+")
texto.write('Texto nuevo que va a pisar todo.')
texto.close()

texto = open("C:\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "r+")
lineas = texto.readline() #lee una sola vez
print(lineas)

texto.write('línea nueva')
texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "r+")
texto.write('línea nueva')

lineas = texto.readlines()#lee todas las líneas
print(lineas)

texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "w+")
lineas = texto.readlines() #lee todas las líneas
print(lineas)

texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "w+")
texto.write('línea nueva')

texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "w+")
lines = texto.readlines()
print(lines)

texto.write('línea nueva')

texto.close()

texto = open("\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt", "w+")
seek = texto.seek(0)
texto.close()

with open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\texto.txt', 'r') as texto:
   lines = texto.readlines()
   print(lines)

# vaca_txt = open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\arch1.txt', 'r+')
# t = vaca_txt.readline()
# print(t)

# t = input('Ingresá un texto con vaca: ') 
# while (t.lower()).count('vaca')==0:
#    t = input('Ingresá un texto con vaca: ')
# vaca_txt.write(f'{t} \n')
# vaca_txt.close()
  
# vaca_txt = open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\arch1.txt', 'r+')
# todas = vaca_txt.readlines()

# for linea in todas:
#    print(linea.strip('\n'))
# vaca_txt.close()


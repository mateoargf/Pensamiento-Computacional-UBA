# 4. Se tiene un archivo con el siguiente texto:
# Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
# se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe
# “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.


palabra_reemplazar = input('Qué palabra desea reemplazar?\n ')

palabra_nueva = input('Por cúal palabra desea reemplazar?\n')

archivo_lectura = open('\\Users\\mateo\\OneDrive\\Documentos\\UBA\\Lic. DS y Pure Math\\cbc\\materias\\pensamiento computacional ubaxxi\\actividades\\guía 8 archivos\\ejercicios\\texto.txt', 'r', encoding='utf-8')
texto= archivo_lectura.readlines()

archivo_lectura.close()

archivo_escritura = open('\\Users\\mateo\\OneDrive\\Documentos\\UBA\\Lic. DS y Pure Math\\cbc\\materias\\pensamiento computacional ubaxxi\\actividades\\guía 8 archivos\\ejercicios\\texto.txt', 'w', encoding='utf-8')

for line in texto:
   archivo_escritura.write(line.lower().replace(palabra_reemplazar, palabra_nueva))
   
archivo_escritura.close()

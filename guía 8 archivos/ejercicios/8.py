# Santi le fue mostrando colores a sus amigos y cada amigo le fue diciendo si le gusta o no. Guardó cada
# respuesta en un .csv de la siguiente manera: nombre;color;le gusta, pero se dió cuenta que no es una
# forma muy práctica de guardarlo, así que lo quiere cambiar. Hacer un programa que lea el archivo y lo
# transforme en un archivo .txt. Es decir que si se tiene un archivo csv de la siguiente forma:

def leer_info(nombre_archivo):
   with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
      info = [linea.strip('\n') for linea in archivo]
         
   return info

def transformar_a_texto(csv_archivo, txt_archivo):
   lineas = leer_info(csv_archivo)
   
   with open(txt_archivo, 'w', encoding='utf-8') as archivo:
      for linea in lineas:
         campos = [campo.strip('\n') for campo in linea.split(';')]
         nombre,color,le_gusta = campos
         if le_gusta.lower() == 'si':
            texto = f'A {nombre} sí le gusta el {color}'
         else:
            texto= f'A {nombre} no le gusta el {color}'
         archivo.write(texto + '\n')
         
transformar_a_texto('guía 8 archivos\\ejercicios\\colores.csv', 'guía 8 archivos\\ejercicios\\colores.txt')
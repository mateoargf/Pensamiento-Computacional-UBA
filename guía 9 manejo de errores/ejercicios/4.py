# 4. Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este
# archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”.

def leer_archivo( nombre_txt='guía 9 manejo de errores\\ejercicios\\file.txt'):
   try : 
      with open(nombre_txt, 'r', encoding='utf-8') as archivo:
         print('Archivo encontrado.')
   except FileNotFoundError:
      print(f'No se pudo encontrar el archivo: {nombre_txt}.')

leer_archivo()
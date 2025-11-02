# 7. En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
# sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
# leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula
# Por ejemplo si se tienen los siguientes archivos:

def leer_info(nombre_archivo):
   archivo = open(nombre_archivo)
   
   info = archivo.readlines()

   for i in range(len(info)):
      info[i] = info[i].strip('\n')
   
   archivo.close()
   return info
      
peliculas = leer_info('guía 8 archivos\\ejercicios\\peliculas.txt')
salas = leer_info('guía 8 archivos\\ejercicios\\salas.txt')

nuevo_archivo = open('guía 8 archivos\\ejercicios\\funciones.csv', 'w', encoding='utf-8')

for i in range(len(peliculas)):
   nuevo_archivo.write(salas[i] + ';' + peliculas[i] + '\n')
nuevo_archivo.close()
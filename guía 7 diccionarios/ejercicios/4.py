# 4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene
# para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace
# mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que
# vio.
# Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista
# de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.

def pelis_fav(listado):
   mejores_pelis = []
   for peli in listado:
      if peli['puntaje'] > 7:
         mejores_pelis.append(peli)
   print(mejores_pelis)

def guardad_peli(listado, nombre, fecha_estreno, puntaje):
   peli_nueva = {
      'nombre': nombre,
      'estreno': fecha_estreno,
      'puntaje': puntaje
   }
   listado.append(peli_nueva)

peliculas = []

guardad_peli(peliculas, 'Piratas del caribe', 2003, 10)
guardad_peli(peliculas, "El Señor de los Anillos", 2001, 10)
guardad_peli(peliculas, "Matrix", 1999, 9)
guardad_peli(peliculas, "Inception", 2010, 7)
guardad_peli(peliculas, "Interstellar", 2014, 9)
guardad_peli(peliculas, "Avengers: Endgame", 2019, 6)
guardad_peli(peliculas, "Gladiador", 2000, 9)
guardad_peli(peliculas, "Forrest Gump", 1994, 7.5)
guardad_peli(peliculas, "Jurassic Park", 1993, 8)
guardad_peli(peliculas, "Toy Story", 1995, 8)
guardad_peli(peliculas, "Catwoman", 2004, 5)
guardad_peli(peliculas, "The Room", 2003, 3)

pelis_fav(peliculas)
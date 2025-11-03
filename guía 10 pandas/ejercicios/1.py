import pandas as pd

peliculas = {'nombre': ['Titanic', 'Kil Bill', 'Matrix', 'El padrino', 'Avatar',
                        'Casablanca', 'El exorcista',  'Soy leyenda',
                        'El club de la pelea', 'Mujercitas'],
            'director': ['James Cameron', 'Quentin Tarantino', 'Hermanas Wachowski',
                        'Francis Ford Coppola', 'James Cameron', 'Michael Curtiz',
                        'William Friedkin', 'Francis Lawrence','David Fincher',
                        'Greta Gerwig'],
            'año': [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
            'género': ['romance', 'acción', 'ciencia ficción', 'drama', 'ciencia ficción', 'drama', 'terror',
                        'ciencia ficción', 'drama', 'drama'],
            'puntaje': [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0]}

df = pd.DataFrame(peliculas)
print(df)

# info = df.info()

# cant_null = df.isnull().sum()
# print(f'la cantidad de valores nulos son\n{cant_null}')

# 2. Mostrar sólo los nombres de las primeras 3 películas del DataFrame
mostrar_nombres = df.loc[:2, ['nombre']]
# print(mostrar_nombres)

# 3. Mostrar sólo el director y el género de todas las películas
df[['director','género']]

# 4. Mostrar las películas que sean de drama.
df.loc[df['género'] == 'drama']

# 5. ¿Qué cantidad de películas hay de cada género?
df['género'].value_counts()

# 6. Mostrar las películas que tengan puntaje entre 6 y 8 y cuyo año de estreno sea anterior a los 2000
df[(df['puntaje'] >= 6) & (df['puntaje'] <= 8)]

# 7. Mostrar las películas que no hayan sido puntuadas (que el puntaje tenga un valor nulo).
df[df['puntaje'].isnull()]

# 8. Calcular el promedio del puntaje de todas las películas.
promedio = df['puntaje'].mean()
# print(promedio)

# 9. Ordenar las películas en orden alfabético descendente.
orden_desc = df.sort_values(by='nombre', ascending=True)
# print(orden_desc)

# 10. Mostrar las 3 películas más antiguas.
antiguedad = df.sort_values(by='año', ascending=True).head(3)
# print(antiguedad)

# 11. Mostrar sólo el nombre y el año de las 3 películas más nuevas.
mas_nuevas = df.sort_values(by='año', ascending=False).head(3).loc[:,['nombre', 'año']]
# print(mas_nuevas)

# 12. Agregar una columna que indique si la película fue vista, o no. Una película fue vista cuando tiene
# puntaje no nulo

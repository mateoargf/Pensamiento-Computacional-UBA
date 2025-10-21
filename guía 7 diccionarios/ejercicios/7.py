# 7. Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y
# todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el
# puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
# a. Crear el diccionario que represente esta situación.
# AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada
# maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las
# maratones? ¿Y qué tipo de dato es la maratón en sí? Debe de ser una lista o tupla que contenga diccionarios de las maratones
# b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
# c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una
# de forma ascendente.

def orden_alfabetico(listado):
    listado.sort(key=lambda x: x['nombre'])
    return listado
   
maratonistas = [
    {
        "nombre": "Mateo Gomez",
        "DNI": "12345678",
        "maratones": [
            {"nombre": "Maratón Buenos Aires", "año": 2022, "puesto": 5, "tiempo": 180},
            {"nombre": "Maratón Nueva York", "año": 2023, "puesto": 3, "tiempo": 175},
            {"nombre": "Maratón Madrid", "año": 2021, "puesto": 8, "tiempo": 190}
        ]
    },
    {
        "nombre": "Ana Lopez",
        "DNI": "87654321",
        "maratones": [
            {"nombre": "Maratón Buenos Aires", "año": 2022, "puesto": 2, "tiempo": 160},
            {"nombre": "Maratón Barcelona", "año": 2023, "puesto": 4, "tiempo": 165},
            {"nombre": "Maratón Madrid", "año": 2021, "puesto": 6, "tiempo": 170}
        ]
    },
    {
        "nombre": "Juan Perez",
        "DNI": "11223344",
        "maratones": [
            {"nombre": "Maratón Buenos Aires", "año": 2022, "puesto": 10, "tiempo": 200},
            {"nombre": "Maratón Nueva York", "año": 2023, "puesto": 7, "tiempo": 195}
        ]
    }
]

print(orden_alfabetico(maratonistas))

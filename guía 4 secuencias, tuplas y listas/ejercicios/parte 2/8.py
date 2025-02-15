# Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia tupla y guarda en ella a todos los que quiere invitar.
# 8. Si alguien cancela tienen que sacarlo de la tupla.
# Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado por parámetro.
# Las tuplas son inmutables, entonces ¿Cómo podemos hacer para “eliminar” un elemento de una tupla?
# Recordemos que las tuplas tienen definido el operador +, pero no el operador -.

# Recibe una tupla y un nombre, devuelve la nueva tupla sin el nombre del parámetro
def eliminar_invitado(tupla, nombre):
    respuesta =  tuple(i for i in tupla if i != nombre)
    return respuesta

invitados_1 = ("Ana", "Carlos", "Elena", "Javier", "Mariana")  
invitados_2 = ("Roberto", "Lucía", "Fernando", "Sofía", "Daniel")

tupla1 = eliminar_invitado(invitados_1, "Carlos")
tupla2 = eliminar_invitado(invitados_2, "Lucía")

print(tupla1)
print(tupla2)
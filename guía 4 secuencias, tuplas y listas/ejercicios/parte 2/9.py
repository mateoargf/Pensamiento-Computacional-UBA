# 9. Cuando ya tienen a todos los invitados tienen que juntar sus tuplas, para eso se necesita una función que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas.
def eliminar_invitado(tupla, nombre):
    respuesta =  tuple(i for i in tupla if i != nombre)
    return respuesta

# Recibe dos parámetros tipo tupla y devuelve una sola tupla
def unir_tuplas(tupla1,tupla2):
     respuesta = tuple(tupla1 + tupla2)
     return respuesta

invitados_1 = ("Ana", "Carlos", "Elena", "Javier", "Mariana")  
invitados_2 = ("Roberto", "Lucía", "Fernando", "Sofía", "Daniel")

tupla1 = eliminar_invitado(invitados_1, "Carlos")
tupla2 = eliminar_invitado(invitados_2, "Lucía")

lista_final = unir_tuplas(tupla1,tupla2)

print(lista_final)
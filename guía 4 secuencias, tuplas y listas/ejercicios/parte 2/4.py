# 4. Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos.
# Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento que se desea insertar no se encuentra en la lista. La lista de ingredientes la podemos pensar como una lista de strings.
# Ejemplo:
# ingredientes: [“tomate”, “queso”, “cebolla”, “huevo”]
# ingrediente a agregar: “orégano”
# La lista de ingredientes debería quedar [“tomate”, “queso”, “cebolla”, “huevo”, “orégano”]
# En cambio, si el ingrediente a agregar es “queso” la lista debería quedar igual.

# Recibe un parámetro y recibe nuevos ingredientes en la lista de str
def agregar_ingredientes(lista):
     ingresar = str(input('Ingrese su nuevo ingrediente y "X" para salir: '))
     while not(ingresar in lista):
          if ingresar in lista:
               break
          else:
               lista.append(ingresar)
          ingresar = str(input('Ingrese su nuevo ingrediente y "X" para salir: '))
     return lista

ingredientes = ['tomate', 'queso', 'cebolla', 'huevo', 'orégano']

nueva_lista = agregar_ingredientes(ingredientes)

print(nueva_lista)
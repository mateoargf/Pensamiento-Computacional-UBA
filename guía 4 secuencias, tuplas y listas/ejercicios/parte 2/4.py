# 4. Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos.
# Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento que se desea insertar no se encuentra en la lista. La lista de ingredientes la podemos pensar como una lista de strings.
# Ejemplo:
# ingredientes: [“tomate”, “queso”, “cebolla”, “huevo”]
# ingrediente a agregar: “orégano”
# La lista de ingredientes debería quedar [“tomate”, “queso”, “cebolla”, “huevo”, “orégano”]
# En cambio, si el ingrediente a agregar es “queso” la lista debería quedar igual.

# Recibe un parámetro y recibe nuevos ingredientes en la lista de str
def agregar_ingredientes(lista):
     ingresar =''
     while ingresar != 'X':
          ingresar = str(input('Ingrese su nuevo ingrediente, "X" si desea salir: '))
          
          if ingresar == 'X':
               break
          elif ingresar in lista:
               ingresar = str(input('ingrese un producto que no esté en la lista, "X" si desea salir: '))
               if ingresar == 'X':
                    break
          else:
               lista.append(ingresar)
     return(print(f'Lista actual: {lista}'))

ingredientes = ['tomate', 'queso', 'cebolla', 'huevo', 'orégano']

agregar_ingredientes(ingredientes)
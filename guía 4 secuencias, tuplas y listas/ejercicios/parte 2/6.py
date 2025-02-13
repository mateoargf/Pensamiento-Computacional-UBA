# 6. Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad de gustos diferentes que tiene que pedir.
# Podemos pensar la lista de empanadas como una lista de strings, entonces deberíamos devolver la cantidad de strings diferentes que hay en una lista.

# Recibe un parámetro y devuelve la cantidad de variedades de empanadas
def devolver_variedades(lista):
     variedades = 0
     gustos = []
     for i in lista:
          if i in gustos:
               continue
          else:
               gustos.append(i)
               variedades += 1
     return variedades
                    

empanadas = ['jamón y queso', 'cebolla', 'capresse', 'humita', 'carne picante', 'carne cortada', 'verdura', 'jamón y queso', 'carne picante', 'jamón y queso', 'verdura', 'roquefort y jamón']

variedad = devolver_variedades(empanadas)

print(f'Las variedades de gustos son: {variedad}')
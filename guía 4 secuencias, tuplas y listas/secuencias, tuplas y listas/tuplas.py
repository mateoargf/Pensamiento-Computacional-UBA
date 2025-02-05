# Tuplas: 
# a = (8, 2, 5) -> a es una tupla (a,b,3)
# a[0] = 1 -> Error: las tuplas no puedes ser modificadas una vez definidas

# ¿Cómo modificamos una tupla?
# a = (1,2)
# a = a*3 # ->  debemos pisarlo, es decir, asignar la nueva tupla
# print(a)

# Recibe un parámetro de la tupla con opciones del menú
def menu(opciones):
     print('Selecciona una opción')
     
     for i in range(1, len(opciones)):
          print(f'{i}-{opciones[i]}') 
             
     opc = int(input())
     
     while opc not in range(1, len(opciones)):
          opc = int(input())
     return opc

quesos=('','cheddar','dambo','muzzarela','brie','cremoso','sin queso')
panes=('','semillas','árabe','centeno','pebete','francés')
carnes=('','hamburguesa','jamón cocido','jamón, crudo','lomito','salchicha','mortadela','veggie')
salsas=('','mayonesa','guacamole','ketchup','salsa golf','barbacoa', 'ranch','sin salsa')
acomp=('','tomate','lechuga','pepinillos','verduras cocidas','berenjena escabeche','sin extras')

print('Armá tu sandwich')
op1=menu(panes)
op2=menu(carnes)
op3=menu(quesos)
op4=menu(acomp)
op5=menu(salsas)

print('Tu pedido de sandwich de pan',panes[op1],'saldrá pronto')
print('Detalle:',carnes[op2],quesos[op3],acomp[op4],salsas[op5],sep='\n')

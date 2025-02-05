#  Accediendo a los elementos de una secuencia

lis= [1,2,3]

print(lis[1])

lis= [1,(1,0,2), 3]
# para referenciar al elemento 2 que es el tercer elemento de una tupla que a su vez ocupa el segundo elemento de las lista
print(f'scope de list -> valor = {lis [1] [2]}')

lis=[('uno', 'dos', 'tres'),(1,2,3)]

# ¿Cuántos niveles debes indicar para referenciar la u de uno ? -> 3
# Observamos que tenemos una lista con dos elementos y cada uno es una tupla con tres elementos. La segunda tupla tiene elementos simples (no son estructuras o iterables), números; mientras que la primera tiene tres elementos que son una secuencia cada uno.

print(f'"u de uno" scope -> valor = {lis[0][0][0]}')

# arma menú de opciones y devuelve selección entera recibe tupla con opciones de menú
def menu(opciones):
     print('Selecciona una opción')
     for i in range(1,len(opciones)):
          print(i,'-',opciones[i][0])
     opc=int(input())
     while opc not in range(1,len(opciones)):
          opc=int(input())
     return opc

quesos=('',('cheddar',75), ('dambo',60), ('sin queso',0))
panes=('',('árabe',70), ('pebete',70), ('francés',60))
carnes=('',('hamburguesa',200), ('jamón cocido',150), ('lomito',200), ('salchicha',100), ('veggie',0))
sand=[]
print('Armá tu sandwich')
op1=menu(panes)
sand.append(panes[op1][1])
op2=menu(carnes)
sand.append(carnes[op2][1])
op3=menu(quesos)
sand.append(quesos[op3][1])
print('Tu pedido de sandwich de pan',panes[op1][0],'saldrá pronto')
print('Detalle:',carnes[op2][0],quesos[op3][0],sep='\n')
print('Abonar: $%.2f'%sum(sand))
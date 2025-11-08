import matplotlib.pyplot as plt

# x = [0,2,10,11,18,25]
# y = [0,1,2,3,4,5]

# fig = plt.figure() # Se crea una figura vacía sin Axes
# plt.plot(x,y) # Agregar ploteo (gráfico de linea)
# plt.show() # Mostrar

# otra alternativa para el gráfico
# fig, ax = plt.subplots()# Se crea una figura con un único Axes.
# ax.plot(x, y) # Agregar los ploteos individuales (gráfico de linea)

# plt.show() # Mostrar

x = [0,2,10,11,18,25] # Tiempo (min)
y = [0,1,2,3,4,5] # Distancia (m)

fig, ax= plt.subplots()
ax.plot(x, y, color='green', marker='^', linestyle='--', markersize=8, linewidth= 1.2)

# Mostrar el título del gráfico
ax.set_title('Gráfico de posición')

# Mostrar el título de los ejes
ax.set_xlabel('Tiempo (min)')
ax.set_ylabel('Distancia (m)')

# Agregar la refencia
ax.legend()

# Grilla preestablecida
ax.grid()

#Grilla modificada
ax.grid(axis='y', color='gray', linestyle='dashed')
plt.show()

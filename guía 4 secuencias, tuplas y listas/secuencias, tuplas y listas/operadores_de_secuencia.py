# Operadores de Secuencias:
x in s # -> Devuelve True si x pertenece a s, False, en caso contrario
s + t # -> Concatena la secuencia s y la t en ese orden
s*n # -> Concatena n veces la secuencia s
s[i] # -> Referencia el elemento de la posición i de la secuencia s
s[-k] # -> Referencia el elemento que está k posiciones antes del final
s[i:j] # -> Referencia la porción de la secuencia s que va del elemento i al j-1
s[i:j:k] # -> Referencia la porción de la secuencia s que va del elemento i al j-1, con paso k
>,<,>=,<=,!=,== # ->Se pueden comparar dos secuencias comparables
len(s) # -> Devuelve la longitud de la secuencia s
min(s) # -> Devuelve el mínimo elemento de s
max(s) # -> Devuelve el máximo elemento de s
sorted(s) # -> Devuelve s ordenada en forma de lista
reversed(s) # -> Devuelve s invertida
s.count(x) # -> Devuelve el número total de ocurrencias de x en s
s.index(x[, i[,j]]) # -> Devuelve el índice de la primera ocurrencia de x en s (en la posición i o superior, y antes de j)

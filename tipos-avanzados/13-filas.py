from collections import deque 

fila = deque([1,2]) #deque es una clase
# fila.append(3)
# fila.append(4)
# fila.append(5)

print(fila)

#para elminar 
fila.popleft()
fila.popleft()
print(fila)

#para verificar si la fila esta vacia
if not fila:
    print("La fila esta vacia")
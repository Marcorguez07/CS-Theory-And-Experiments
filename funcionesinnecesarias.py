# Informatica
# Documento de funciones innecesarias que aún así necesito aprender.

# 1.) ENUMERATE

# Enumerate imprime el indice y el valor actual del iterado. Requiere de dos valores.
def enumeratetest(x):
    for indx, value in enumerate(x):
        print(indx, value)

# a enumerate se le puede añadir un segundo parametro que es el indice de donde empezar a enumerar en una secuencia dada.

enumeratetest(["manzana", "pera", "aguacate"])


# 2.) LIST.CLEAR()    

#En Python, list.clear() es un método de listas que se utiliza para eliminar todos los elementos de la lista, dejándola vacía.

list1 = [1,2,3,4]
print(list1)
list1.clear() # no acepta parametros, limpia todo.
print(list1)

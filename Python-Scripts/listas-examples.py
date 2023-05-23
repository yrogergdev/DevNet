# numbers = [10, -5, 7.0, "Greg", "1"]
# print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.
# print(numbers[3])
# print(len(numbers))
# numbers[0] = 111
# print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.
 
# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# ###

# del numbers[1]  # Eliminando el segundo elemento de la lista.
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# ###
# print(numbers[-5])
# #numbers[4] = 1

# hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# # Paso 1: escribe una línea de código que solicite al usuario
# # reemplazar el número de en medio con un número entero ingresado por el usuario.
# hat_list[2] = int(input("Ingrese un número entero: "))
# # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
# del hat_list[-1]
# # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
# print(len(hat_list))
# print(hat_list)
# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)

# print(my_list)

# my_list = []  # Creando una lista vacía.
 
# for i in range(5):
#     my_list.insert(0, i + 1)
 
# print(my_list)
# print(3//2)

# import tkinter as tk
# from tkinter import ttk

# def greet():
#     print("Hello, world")

# root = tk.Tk()
# root.config(width=500, height=500)
# root.title("Button in Tk")
# button = ttk.Button(text="Hello, world!", command=greet)
# button.place(x=50, y=50)
# root.mainloop()

#my_list = [8, 10, 6, 2, 4]  # lista a ordenar

swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
my_list = []
test = []
pasos = 0
num = int(input("¿Cuántos elementos deseas ordenar?: "))
for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)
    #test.append(val)

print("Lista ingresada: ", my_list)
test = my_list.copy()
print("Lista test: ", test)
print("Lista ingresada: ", my_list)
test.sort()
print("""Lista ordenada con clase Sort():""" , test, "\nLista ingresada", my_list)

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            print("intercambio")
            pasos += 1
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#my_list[4] = 11
test[4] = 0
print("\nLista Ordenada; ", my_list)
print("\nLista test; ", test)
print("\nCandidad de intercambios ejecutados:", pasos)

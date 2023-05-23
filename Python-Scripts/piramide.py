blocks = int(input("Ingresa el número de bloques: "))
blocks2 = blocks
height = 0
level = 1
blocks_left = 0
if blocks <=1:
        print("Fin del trabajo, minima cantidad de bloques para hacer la piramide")
else :
        while height < blocks:
            blocks = blocks - level
            blocks_left = blocks
            height = height + 1
            level = level + 1
print("La altura de la piramide:", height)
print("Cantidad de bloques restantes: ", blocks)
print("El numero de bloques para armar la piramide sin sobrantes mas cercano al ingresado es: ", (blocks2 - blocks_left))
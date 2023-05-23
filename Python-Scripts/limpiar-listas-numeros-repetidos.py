import copy

my_list = [1,3,3,4,5,1,10,11,20,13,14,14,14,20,20,10,-1,-1,-0,-1]
my_list2 = []

for i in my_list:
     if i not in my_list2:
        my_list2.append(i)

print("La lista con elementos únicos:")
print(my_list2)

squares = [x ** 2 for x in range(10)]
print(squares)
odds = [x for x in squares if x % 2 != 0 ]
print(odds)

board = []
EMPTY = ["PEON"]
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
print(board)
print(len(board))

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
total = 0.0
temps[0][11] = 12.0
for day in temps:
    print(day)
    total += day[11]
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average)
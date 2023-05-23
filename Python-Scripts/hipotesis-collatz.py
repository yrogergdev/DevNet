
c0 = int(input("Ingresa un numero: "))
counter = 0
a = c0

if a >0:
    while c0 !=1:
            if c0 % 2 == 0:
                c0 = c0/2
                if c0 != 1:
                      counter +=1
                      print(int(c0))
                      continue
                else:
                      counter +=1
                      print(int(c0))
                      break
            elif  c0 % 2 ==1:
                    c0 = int((c0*3) +1)
                    if c0 != 1:
                        counter +=1
                        print(int(c0))
                        continue
    print("Pasos: ", counter)
else : 
    print("Error ingresaste un numero negativo o cero")






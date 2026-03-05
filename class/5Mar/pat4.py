# Primary Diagonal : i == j
#lower triangle in terms of primary: i > j
#upper triangle in terms of primary: j > i

# Secondary Diagonal: i + j == rows + 1
#lower triangle in terms of secondary: i + j > rows + 1
#upper triangle in terms of secondary: j + i < rows + 1

for i in range (1, 10):
    for j in range(1, 10):
        if (i + j > 9 +1): #lower
            print("@", end=" ")
        elif(i + j < 9 + 1): #upper
            print("*", end=" ")
        elif(i + j == 9+1):
            print("#",end=" ")
        else:
            print(" ", end=" ")
    print()
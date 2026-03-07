for i in range(4):
    for j in range(4):
        if (i == j): #diagonal
            print("*", end=' ')
        elif(i > j): #lower triangle
            print("#", end=' ')
        elif(j > i): #upper triangle
            print("@", end=" ")
    print()
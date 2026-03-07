for i in range(1, 4):
    for j in range(1, 4):
        if (i + j == 3 + 1):
            print("#", end=" ")
        elif(i == j):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
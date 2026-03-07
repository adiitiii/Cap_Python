#Secondary Diagonal
r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

for i in range(r):
    for j in range(c):
        if (i + j == r+1): #diagonal
            print("#", end=' ')
        else:
            print(" ", end=' ')
    print()
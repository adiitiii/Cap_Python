#print initial index of a char present in a given string
# n = input("Enter a string: ")
# m = input("Enter the char: ")

def alphaPresent(n, m, z, v, y, u, i, o):
    for i in range(0, len(n)):
        if(n[i] == m):
            return i
    print("Not present")

print(alphaPresent(n,m,z,v,y,u,i,o))
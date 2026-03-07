l = [1, 2, 3, 4, 5, 6, 7]
def add(l):
    s = 0
    for i in range(0, len(l)):
        if len(l) >= 2 and len(l) <= 5:
            s += l[i]
            # print("No summation can be performed")
    print(s)

add(l)
# print(len(l))



#Q2: WAP to find out sum of individual digits of nu,=m
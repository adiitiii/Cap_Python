#to find the sum of digits in a number

n = input("Enter num: ")

def dig(n):
    s=0
    for i in n:
        s += int(i)
    return s

print(dig(n))
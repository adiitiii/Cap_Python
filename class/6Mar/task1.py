n = eval(input("Enter a list of integers : "))
def prod(n):
    product = 1
    for i in n:
        product *= i
    print(product)
prod(n)


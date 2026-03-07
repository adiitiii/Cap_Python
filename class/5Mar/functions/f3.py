a = 1234
def name():
    global a
    a= 20
    b=200
    def name2():
        nonlocal b
        b = 300
name()
print(a)
print(b)

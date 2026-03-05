s = input("Enter your name: ")
temp = ''
for i in s:
    if(i == ' '):
        temp += '_'
    else:
        temp += i
print(temp)
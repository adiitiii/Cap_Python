s = input("Enter a string here: ")
temp = ''
i = len(s)-1
while(i >= 0):
    temp += s[i]
    i-=1
print(temp)
i = 'aaabbaabcc'
count = 1
for x in range(0, len(i)-1):
    if(i[x] == i[x+1]):
        count+=1
        x+=1
    else:
        print(f'{i[x]}' + f'{count}', end="")
        count = 1
        x+=1
print(f'{i[x]}' + f'{count}', end="")

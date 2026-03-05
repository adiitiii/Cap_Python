l = [(2+3j), 12, 'Program','Python',False]
d={}
vowels = 'aeiouAEIOU'
for i in l:
   if type(i) == str:
    v=''
    for j in i:
        if j in vowels:
            v += j
    d[i] = v
print(d)
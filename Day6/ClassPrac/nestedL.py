l = ['Aditi','Srvsh','Pradipt','Bhavik']
v=''
for i in l:
    for j in i:
        if j in 'aeiouAEIOU':
            v += j
print(v)
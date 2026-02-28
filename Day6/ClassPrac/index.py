l = ['p1.py', 'first.txt', 't3.py', 'tk.txt', 'tfk.com']
d = {}
for item in l:
    ext = item.split('.')
    print(ext)

    if ext[1] in d:
        d[ext[1]].append(ext[0])
    else:
        d[ext[1]] = [ext[0]]
print(d)
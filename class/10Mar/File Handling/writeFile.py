#WRITE      overwrites the data, creates a new file if the mentioned file does not exists
file = open('temp.txt', 'w+')
file.writelines([
    'I am the first\n', 
    'yo line\n',
    'third line\n'
    'fourth line\n',
    'fifth line\n',
    'sixth line\n',
    'seventh line\n',
])
file.seek(0)
print(file.read())

file.close()

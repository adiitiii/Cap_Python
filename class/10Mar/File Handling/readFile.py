file = open('temp.txt', 'r')
'''
1. read(): display the file content as it is
2. readline(): displays single line of data at a time
3. readlines(): displays all the content in a single list separated with '\n' just as how we wrote it in  the 
                writelines function
'''

print(file.read()) #all data at once

file.seek(0)
for i in range(8):
    print(file.readline()) #all data but single line it reads

file.seek(0)
print(file.readlines())
file.close()
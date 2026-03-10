file = open('jecrc.txt', 'a+')
# file.write('JECRC is a very blah Uni\n')
# file.write('JECRC is also popular for placements')

file.writelines([
    '\nfood is good\n',
    'ECO system is good\n',
    'faculties are very supportive\n',
])
file.seek(0)
print(file.read())

file.close()
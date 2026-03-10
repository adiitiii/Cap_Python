import csv
from datetime import date

file = open('expense.csv', 'a+', newline ='')
# w = csv.writer(file)
r = csv.reader(file)
file.seek(0)

print(list(r)) #explicit typecasting is needed else it will print its object

# w.writerow([ 'DATE', 'CATEGORY', 'AMOUNT' ]) ##column heads
# w.writerows( #for column data
#     [
#         [date.today(), 'Travel', 2000],
#         [date.today(), 'Food', 550],
#         [date.today(), 'Entertainment', 1075],
#     ]
# )



file.close()
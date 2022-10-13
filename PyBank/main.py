from itertools import count
import os
from csv import reader

months = 0
net = 0
biggest = 0
smallest = 0
changes = []

os.chdir(os.path.dirname(os.path.realpath(__file__)))
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # iterate through rows in csvfile
    for row in csvreader:
        
        # adding change in profits/losses if not the first row
        if months != 0:
            changes.append(int(row[1]) - last_change)
        
        # checking for and assigning biggest change
        if int(row[1]) > biggest:
            biggest = int(row[1])
            biggest_date = row[0]

        # checking for and assigning smallest change
        if int(row[1]) < smallest:
            smallest = int(row[1])
            smallest_date = row[0]

        # saving last change for above calculation
        last_change = int(row[1])

        # adding a month
        months += 1

        # calculating sum
        net += int(row[1])

# output to txt file
with open('analysis\data.txt','w') as f:
    f.write('Financial Analysis \n----------------------------\n')
    f.write(f'Total Months: {months}\n')
    f.write(f'Total: ${net}\n')
    f.write(f'Average change: ${round(sum(changes)/len(changes),2)}\n')
    f.write(f'Greatest Increase in Profits: {biggest_date} (${biggest})\n')
    f.write(f'Greatest Decrease in Profits: {smallest_date} (${smallest})\n')

print('\n\nFinancial Analysis \n----------------------------')
print(f'Total Months: {months}')
print(f'Total: ${net}')
print(f'Average change: ${round(sum(changes)/len(changes),2)}')
print(f'Greatest Increase in Profits: {biggest_date} (${biggest})')
print(f'Greatest Decrease in Profits: {smallest_date} (${smallest})\n')
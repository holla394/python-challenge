from lib2to3.pgen2.token import COMMA
import pandas as pd

data = pd.read_csv("~\Bootcamp\challenges\python-challenge\PyBank\Resources\Budget_Data.csv",',',None,0)

count = 0
net = 0
biggest = 0
smallest = 0
changes = []
for index,series in data.iterrows():
    # show output of data series:
    # print(series.name)
    # print(series.values[0])
    # print(series.values[1])
    
    # calculating sum
    net = net + series.values[1]

    # checking for and assigning biggest change
    if series.values[1] > biggest:
        biggest = series.values[1]
        biggest_date = series.values[0]
    
    # checking for and assigning smallest change
    if series.values[1] < smallest:
        smallest = series.values[1]
        smallest_date = series.values[0]

    # adding change in profits/losses if not the first row
    if index != 0:
        changes.append(series.values[1] - last_change)

    # saving last change for above calculation
    last_change = series.values[1]

""" # desired output to terminal:
print('\n\nFinancial Analysis \n---------------------------- ')
print(f'Total Months: {len(data)}')
print(f'Total: ${net}')
print(f'Average change: ${round(sum(changes)/len(changes),2)}')
print(f'Greatest Increase in Profits: {biggest_date} (${biggest})')
print(f'Greatest Decrease in Profits: {smallest_date} (${smallest})') """

# output to txt file
with open('analysis\data.txt','w') as f:
    f.write('Financial Analysis \n----------------------------\n')
    f.write(f'Total Months: {len(data)}\n')
    f.write(f'Total: ${net}\n')
    f.write(f'Average change: ${round(sum(changes)/len(changes),2)}\n')
    f.write(f'Greatest Increase in Profits: {biggest_date} (${biggest})\n')
    f.write(f'Greatest Decrease in Profits: {smallest_date} (${smallest})\n')
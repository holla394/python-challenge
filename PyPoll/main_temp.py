# import pandas as pd

# data = pd.read_csv('~/Bootcamp/Challenges/python-challenge/PyPoll/Resources/election_data.csv',',',None,0)
# print(len(data))

# print(data.shape)
# print(len(data))
# #print(index)
# print(data.index)
# print(data.values)

# for index,series in data.iterrows():
#     print(len(data))
#     print(index)

# import csv
from itertools import count
import os
from csv import reader
csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
print(csvpath)
# csvpath = os.path.join('c','Users','e1317395','Bootcamp','Challenges','python-challenge','PyPoll','Resources','election_data.csv')
# print(csvpath)

vote_cntr = 0
charles = 0
diana = 0
raymon = 0
with open(csvpath) as csvfile:
    csvreader = reader(csvfile, delimiter = ',')
    print(f'Reading CSV file:{csvreader}')
    csv_header = print(next(csvreader))

    for row in csvreader:
        vote_cntr += 1
        if "Charles" in row[2]:
            charles += 1
        if "Diana" in row[2]:
            diana += 1
        if "Raymon" in row[2]:
            raymon += 1
    
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {vote_cntr}')
    print('-------------------------')
    print(f'Charles Casper Stockham: {round(100*(charles/vote_cntr),3)}% ({charles})')
    print(f'Diana DeGette: {round(100*(diana/vote_cntr),3)}% ({diana})')
    print(f'Raymon Anthony Doane: {round(100*(raymon/vote_cntr),3)}% ({raymon})')

    with open('analysis\data.txt','w') as f:
        f.write('Election Results\n')
        f.write('-------------------------\n')
        f.write(f'Total Votes: {vote_cntr}\n')
        f.write('-------------------------\n')
        f.write(f'Charles Casper Stockham: {round(100*(charles/vote_cntr),3)}% ({charles})\n')
        f.write(f'Diana DeGette: {round(100*(diana/vote_cntr),3)}% ({diana})\n')
        f.write(f'Raymon Anthony Doane: {round(100*(raymon/vote_cntr),3)}% ({raymon})')
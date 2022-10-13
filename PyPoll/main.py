from itertools import count
import os
from csv import reader

# from sympy import N

# setting directory of this active .py file as it runs
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# setting filepath for csv file to read from
csvpath = os.path.join('Resources','election_data.csv')

# declaring variables
vote_cntr = 0
name_counter = 0
names = []
votes = []

# opening csv file in with block
with open(csvpath) as csvfile:

    # reads csv file header info
    csvreader = reader(csvfile, delimiter = ',')

    # reads first row of csv file (data labels, not the data itself)
    csv_header = next(csvreader)

    # iterating through lines of csv file
    for row in csvreader:
        
        # increment vote count
        vote_cntr += 1

        # adds name to list if new candidate name
        if row[2] not in names:
            names.append(row[2])
            name_counter += 1
            votes.append(1)
        else:
            # adds one vote to "votes" list's index of candidate name
            # indexes of names and votes lists are matching for candidates' vote counts
            votes[names.index(row[2])] += 1

    # printing results to terminal
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {vote_cntr}')
    print('-------------------------')
    # printing out candidate info
    for index in range(len(names)):
        print(f'{names[index]}:{round(100*(votes[index]/vote_cntr),3)}% ({votes[index]})')
    print("-------------------------")
    print(f'Winner: {names[votes.index(max(votes))]}')
    print("-------------------------")

    # printing results to txt file
    with open('analysis\data.txt','w') as f:
        f.write('Election Results\n')
        f.write('-------------------------\n')
        f.write(f'Total Votes: {vote_cntr}\n')
        f.write('-------------------------\n')
        for index in range(len(names)):
            f.write(f'{names[index]}:{round(100*(votes[index]/vote_cntr),3)}% ({votes[index]})\n')
        f.write("-------------------------\n")
        f.write(f'Winner: {names[votes.index(max(votes))]}\n')
        f.write("-------------------------")
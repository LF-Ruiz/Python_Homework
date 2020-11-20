import csv
import os

election_data  = 'Resources\election_data.csv'

#Create variables
total_votes = 0 

with open (election_data) as data:
    data_reader = csv.reader(data, delimiter= ",")
    next(data_reader)

    for row in data_reader:
        total_votes += 1
        
    print(total_votes)

import csv
import os

election_data  = 'Resources\election_data.csv'

#Create variables
total_votes = 0
votes_percent = 0 

with open (election_data) as data:
    data_reader = csv.reader(data, delimiter= ",")
    next(data_reader)

    for row in data_reader:
        total_votes += 1
        
#        pypoll_dict[voting_data[0]] = voting_data[2]
# Define the function and have it accept the 'results' as its sole parameter
#        def percentages(results):
    # For readability, it can help to assign your values to variables with descriptive names
#            voter_id = int(results[0])
#            county = str(results[1])
#            candidate = int(results[2])
    


    # votes percent can be found by dividing the the votes for a candidate  by the total votes and multiplying by 100
#            votes_percent = (candidate / total_votes) * 100


    print(total_votes)
    print(votes_percent)